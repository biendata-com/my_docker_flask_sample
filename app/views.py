from app import app
from flask import request, send_file
import pickle as pkl

@app.route('/')
def home():
   return "Hello Biendata!"

@app.route('/predict', methods=['GET'])
def predict():
   # This is the API function. It will pass parameters to the model function below. And return the output file as response
   
   if 'adj' in request.args and 'feature' in request.args:
      adj = request.args['adj']
      feature = request.args['feature']
      
      result = model(adj, feature)
      
      return send_file(result, attachment_filename='out.pkl', as_attachment=True) 
   else:
      return "Error: Args not found."


def model(adj, feature):
   # You can implement your model here and return the path of the output file.
   
   ########################################################
   '''
   adj = pkl.load(open(adj,'rb'))
   feature = pkl.load(open(feature,'rb'))
   
   processed_adj=GCNadj(adj)
   sparserow=torch.LongTensor(processed_adj.row).unsqueeze(1)
   sparsecol=torch.LongTensor(processed_adj.col).unsqueeze(1)
   sparseconcat=torch.cat((sparserow,sparsecol),1)
   sparsedata=torch.FloatTensor(processed_adj.data)
   adjtensor=torch.sparse.FloatTensor(sparseconcat.t(),sparsedata,torch.Size(processed_adj.shape))
   
   featuretensor=torch.FloatTensor(features)
   featuretensor=Variable(featuretensor,requires_grad=True)
   

   model=GCN_norm(len(dims)-1,dims)

   model.load_state_dict(torch.load('model_norm.pkl',map_location='cpu'))

   out=model(featuretensor,adjtensor,dropout=0)
   pkl.dump(out,open("/application/out.pkl","wb+"))
   return "/application/out.pkl"
   '''
   #######################################################
   
   return '/application/out.pkl'
