# import libraries
import pandas as pd

class Button:
    def __init__(self, window):
        self.window = window
        self.result = pd.read_csv('./result/benchmark_result.csv')
    
    def test(self, values, current_dataset, current_model):
        acc7, acc2, f1, mae, corr, acc5 = values

        if current_model == "EF-LSTM" and current_dataset == "CMU-MOSI":
            acc7["text"] = str(self.result.iloc[0, 6]) 
            acc2["text"] = str(self.result.iloc[0, 2]) 
            f1["text"] = str(self.result.iloc[0, 3])
            mae["text"] = str(self.result.iloc[0, 4])
            corr["text"] = str(self.result.iloc[0, 5])
            acc5["text"] = '-' 
        
        elif current_model == "LMF" and current_dataset == "CMU-MOSI":
            acc7["text"] = str(self.result.iloc[1, 6]) 
            acc2["text"] = str(self.result.iloc[1, 2]) 
            f1["text"] = str(self.result.iloc[1, 3])
            mae["text"] = str(self.result.iloc[1, 4])
            corr["text"] = str(self.result.iloc[1, 5])
            acc5["text"] = '-' 

        elif current_model == "MFN" and current_dataset == "CMU-MOSI":
            acc7["text"] = str(self.result.iloc[2, 6]) 
            acc2["text"] = str(self.result.iloc[2, 2]) 
            f1["text"] = str(self.result.iloc[2, 3])
            mae["text"] = str(self.result.iloc[2, 4])
            corr["text"] = str(self.result.iloc[2, 5])
            acc5["text"] = '-' 

        elif current_model == "CM-BERT (w/o Visual)" and current_dataset == "CMU-MOSI":
            acc7["text"] = str(self.result.iloc[3, 6]) 
            acc2["text"] = str(self.result.iloc[3, 2]) 
            f1["text"] = str(self.result.iloc[3, 3])
            mae["text"] = str(self.result.iloc[3, 4])
            corr["text"] = str(self.result.iloc[3, 5])
            acc5["text"] = '-' 
        
        elif current_model == "CM-BERT (w/ Visual)" and current_dataset == "CMU-MOSI":
            acc7["text"] = str(self.result.iloc[4, 6]) 
            acc2["text"] = str(self.result.iloc[4, 2]) 
            f1["text"] = str(self.result.iloc[4, 3])
            mae["text"] = str(self.result.iloc[4, 4])
            corr["text"] = str(self.result.iloc[4, 5])
            acc5["text"] = '-' 
        
        elif current_model == "EF-LSTM" and current_dataset == "CMU-MOSEI":
            acc7["text"] = str(self.result.iloc[5, 6]) 
            acc2["text"] = str(self.result.iloc[5, 2]) 
            f1["text"] = str(self.result.iloc[5, 3])
            mae["text"] = str(self.result.iloc[5, 4])
            corr["text"] = str(self.result.iloc[5, 5])
            acc5["text"] = '-' 
        
        elif current_model == "LMF" and current_dataset == "CMU-MOSEI":
            acc7["text"] = str(self.result.iloc[6, 6]) 
            acc2["text"] = str(self.result.iloc[6, 2]) 
            f1["text"] = str(self.result.iloc[6, 3])
            mae["text"] = str(self.result.iloc[6, 4])
            corr["text"] = str(self.result.iloc[6, 5])
            acc5["text"] = '-' 
        
        elif current_model == "MFN" and current_dataset == "CMU-MOSEI":
            acc7["text"] = str(self.result.iloc[7, 6]) 
            acc2["text"] = str(self.result.iloc[7, 2]) 
            f1["text"] = str(self.result.iloc[7, 3])
            mae["text"] = str(self.result.iloc[7, 4])
            corr["text"] = str(self.result.iloc[7, 5])
            acc5["text"] = '-' 
        
        elif current_model == "CM-BERT (w/o Visual)" and current_dataset == "CMU-MOSEI":
            acc7["text"] = str(self.result.iloc[8, 6]) 
            acc2["text"] = str(self.result.iloc[8, 2]) 
            f1["text"] = str(self.result.iloc[8, 3])
            mae["text"] = str(self.result.iloc[8, 4])
            corr["text"] = str(self.result.iloc[8, 5])
            acc5["text"] = '-' 
        
        elif current_model == "CM-BERT (w/ Visual)" and current_dataset == "CMU-MOSEI":
            acc7["text"] = str(self.result.iloc[9, 6]) 
            acc2["text"] = str(self.result.iloc[9, 2]) 
            f1["text"] = str(self.result.iloc[9, 3])
            mae["text"] = str(self.result.iloc[9, 4])
            corr["text"] = str(self.result.iloc[9, 5])
            acc5["text"] = '-' 
        
        elif current_model == "EF-LSTM" and current_dataset == "CH-SIMS":
            acc5["text"] = str(self.result.iloc[10, 6]) 
            acc2["text"] = str(self.result.iloc[10, 2]) 
            f1["text"] = str(self.result.iloc[10, 3])
            mae["text"] = str(self.result.iloc[10, 4])
            corr["text"] = str(self.result.iloc[10, 5])
            acc7["text"] = '-' 
        
        elif current_model == "LMF" and current_dataset == "CH-SIMS":
            acc5["text"] = str(self.result.iloc[11, 6]) 
            acc2["text"] = str(self.result.iloc[11, 2]) 
            f1["text"] = str(self.result.iloc[11, 3])
            mae["text"] = str(self.result.iloc[11, 4])
            corr["text"] = str(self.result.iloc[11, 5])
            acc7["text"] = '-' 
        
        elif current_model == "MFN" and current_dataset == "CH-SIMS":
            acc5["text"] = str(self.result.iloc[12, 6]) 
            acc2["text"] = str(self.result.iloc[12, 2]) 
            f1["text"] = str(self.result.iloc[12, 3])
            mae["text"] = str(self.result.iloc[12, 4])
            corr["text"] = str(self.result.iloc[12, 5])
            acc7["text"] = '-' 
        
        elif current_model == "CM-BERT (w/o Visual)" and current_dataset == "CH-SIMS":
            acc5["text"] = str(self.result.iloc[13, 6]) 
            acc2["text"] = str(self.result.iloc[13, 2]) 
            f1["text"] = str(self.result.iloc[13, 3])
            mae["text"] = str(self.result.iloc[13, 4])
            corr["text"] = str(self.result.iloc[13, 5])
            acc7["text"] = '-' 
        
        elif current_model == "CM-BERT (w/ Visual)" and current_dataset == "CH-SIMS":
            acc5["text"] = str(self.result.iloc[14, 6]) 
            acc2["text"] = str(self.result.iloc[14, 2]) 
            f1["text"] = str(self.result.iloc[14, 3])
            mae["text"] = str(self.result.iloc[14, 4])
            corr["text"] = str(self.result.iloc[14, 5])
            acc7["text"] = '-' 