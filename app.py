import time
import torch
import os
from PIL import Image
from torch.autograd import Variable
from torchvision.transforms import ToTensor, ToPILImage

from flask import Flask, jsonify, request, send_file, request

from model import Generator

app = Flask(__name__)

def changeImg():
  upscale_factor = 4
  image_name = './images/result/request.png'
  model_name = 'netG_epoch_4_99.pth'

  model = Generator(upscale_factor).eval()

  model.load_state_dict(torch.load('epochs/' + model_name, map_location=lambda storage, loc: storage))

  image = Image.open(image_name)
  image = Variable(ToTensor()(image), volatile=True).unsqueeze(0)

  start = time.perf_counter()
  out = model(image)
  elapsed = (time.perf_counter() - start)
  out_img = ToPILImage()(out[0].data.cpu())
  out_img.save('images/result/response.png')

@app.route('/') 
def hello():
  return 'hello world!'

@app.route('/img', methods=['POST']) 
def get_file():
  img = request.files['img']
  img.save(os.path.join('./images/result', 'request.png'))
  changeImg()
  return send_file('./images/result/response.png')

if __name__ == '__main__':
  app.run()