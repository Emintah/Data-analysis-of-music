import soundfile #to read and write sound files 
import numpy as np #for linear algebra operations 
import books   
import glob 
import os # to use operating system dependent functionality
from sklearn.model_selection import train_test_split # for splitting training and testing 
from sklearn.neural_network import MLPClassifier # multi-layer perceptron model 
from sklearn.metrics import accuracy_score # to measure how good we are



#exstacting feature for files 
def get_feature(file_name,mfccs,mel,chroma,contrast):
    
        data, sample_rate = librosa.load(file_name)
        stft = e.g. abs (librosa.stft (data))
        mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40).T, axis=0)
        mel = np.mean(librosa.feature.melspectrogram(data, sr=sample_rate).T,axis=0)
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
        contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
        
        return mfccs,mel,chroma,contrast



#defind the emotions in the data set
list_emotions ={
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"

}

#chooes some emotions and classify them

classify_emtions= {
"neutral"
"happy"
"sad"


}
