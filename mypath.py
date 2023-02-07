class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = 'C:/Users/25223/Documents/NUS-CE/deepfake detection/DataSet/celeb-deepfakeforensics-master/celeb-deepfakeforensics-master/ucf101/ucf101'

            # Save preprocess data into output_dir
            output_dir = '/path/to/VAR/ucf101'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = './dataloaders/hmdb51'

            output_dir = './dataloaders/hmdb51_processed'

            return root_dir, output_dir
        elif database == 'kaggle':
            # folder that contains class labels
            root_dir = '../Downloads/deepfake-detection-challenge/train'

            output_dir = './dataloaders/deepfake-processed'

            return root_dir, output_dir
        elif database == 'celeb-df':
            # folder that contains class labels
            root_dir = '/home1/ruipeng/Celeb-v1/Train'

            output_dir = '/home1/ruipeng/Celeb-v1/I3D-processed-cropped'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return './c3d-pretrained.pth'