#From David Schwertfeger in Toward Data Science
#Link: https://towardsdatascience.com/how-to-build-efficient-audio-data-pipelines-with-tensorflow-2-0-b3133474c3c1


import tensorflow as tf


def _bytestring_feature(list_of_bytestrings):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=list_of_bytestrings))


def _int_feature(list_of_ints):  # int64
    return tf.train.Feature(int64_list=tf.train.Int64List(value=list_of_ints))


def _float_feature(list_of_floats):  # float32
    return tf.train.Feature(float_list=tf.train.FloatList(value=list_of_floats))


def to_tfrecord(audio, label):
    feature = {
        'audio': _float_feature(audio),  # audio is a list of floats
        'label': _int_feature([label])  # wrap label index in list
    }
    # Example is a flexible message type that contains key-value pairs,
    # where each key maps to a Feature message. Here, each Example contains
    # two features: A FloatList for the decoded audio data and an Int64List
    # containing the corresponding label's index.
    return tf.train.Example(features=tf.train.Features(feature=feature))


if __name__ == "__main__":
    # Assume a dataset of [audio, label] pairs
    dataset = load_dataset()

    with tf.io.TFRecordWriter('train.tfrecord') as out:
        # Iterate over [audio, label] pairs in dataset
        for audio, label in dataset:
            # Encode [audio, label] pair to TFRecord format
            example = to_tfrecord(audio, label)
            # Write serialized example to TFRecord file
            out.write(example.SerializeToString())
