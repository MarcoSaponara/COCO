from torchtext.datasets import LanguageModelingDataset
from torchtext import data

class CocoDataset(LanguageModelingDataset):
    urls = ['https://github.com/MarcoSaponara/COCO']
    name = 'COCO'
    dirname = 'COCO'

    @classmethod
    def splits(cls, text_field, root='./', train='annotations_train_val_2014/captions_train2014.json',
               validation='annotations_train_val_2014/captions_val2014.json',
               test='annotations_test_2014/image_info_test2014.json', **kwargs):
        """Create dataset objects for splits of the COCO dataset.

        This is the most flexible way to use the dataset.

        Arguments:
            text_field: The field that will be used for text data.
            root: The directory in whose COCO
                subdirectory the data files will be stored.
            train: The filename of the train data.
            validation: The filename of the validation data, or None to not
                load the validation set.
            test: The filename of the test data, or None to not load the test
                set.
        """
        return super(CocoDataset, cls).splits(
            root=root, train=train, validation=validation, test=test,
            text_field=text_field, **kwargs)

    @classmethod
    def iters(cls, batch_size=32, bptt_len=35, device=0, root='./',
              vectors=None, **kwargs):
        """Create iterator objects for splits of the COCO dataset.

        This is the simplest way to use the dataset, and assumes common
        defaults for field, vocabulary, and iterator parameters.

        Arguments:
            batch_size: Batch size.
            bptt_len: Length of sequences for backpropagation through time.
            device: Device to create batches on. Use -1 for CPU and None for
                the currently active GPU device.
            root: The directory in whose COCO
                subdirectory the data files will be stored.
            wv_dir, wv_type, wv_dim: Passed to the Vocab constructor for the
                text field. The word vectors are accessible as
                train.dataset.fields['text'].vocab.vectors.
            Remaining keyword arguments: Passed to the splits method.
        """
        TEXT = data.Field()

        train, val, test = cls.splits(TEXT, root=root, **kwargs)

        TEXT.build_vocab(train, vectors=vectors)

        return data.BPTTIterator.splits(
            (train, val, test), batch_size=batch_size, bptt_len=bptt_len,
            device=device)