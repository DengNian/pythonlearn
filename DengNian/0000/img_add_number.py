from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def img_add_number(image_path,sign="46"):
	im=Image.open(image_path)
	width,height=im.size
	draw=ImageDraw.Draw(im)
	font=ImageFont.truetype("Arial.ttf",min(width//6,height//6))
	draw.text((width*0.75,height*0.075),sign,font=font,fill=(255,33,33,255))
	left,right=image_path.rsplit(".",1)
	new_image_path=left+"_"+sign+"."+right
	im.save(new_image_path)
	
if __name__=='__main__':
	img_add_number("./sample.jpg")
	print"Finished."