from transformers import BertPreTrainedModel
import torch
class RelevanceModel(BertPreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.bert = BertModel(config)
        self.regressor = nn.Linear(config.hidden_size, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        score = self.regressor(pooled_output)
        score = torch.sigmoid(score)
        return score
#Assuming that the scratch_bert pretrained model is located in the following path:
PRETRAIN_PATH="scratch_bert/"
#This is the path of the checkpoint
CHECKPOINT="rel_bert.pth"
if __name__=="__main__":
    model=RelevanceModel.from_pretrained(PRETRAIN_PATH)
    #use map_location to ensure that the model can be loaded with a CPU-only machine
    model.load_state_dict(torch.load(CHECKPOINT,map_location="cpu"))