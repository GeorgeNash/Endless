from imagesoup import ImageSoup

class Hunter():

	IMAGES_WANTED = 5

	def __init__(self):
		self.soup = ImageSoup()

	def hunt(self, word):
		images = self.soup.search(word, n_images=self.IMAGES_WANTED)
		return images
