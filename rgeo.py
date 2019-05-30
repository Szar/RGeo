#!/usr/bin/python
import json
from shapely import geometry

class geocode:
	def __init__(self):
		self.types = ["states","counties"]
		self.data = self.load()

	def load(self):
		data = {}
		for t in self.types:
			data[t] = json.loads(open("./data/"+t+".json", 'r', encoding='utf-8', errors='ignore').read())
			for gid in data[t]:
				data[t][gid]["polygon"] = geometry.Polygon(data[t][gid]["polygon"])
		return data
		
	def search(self, lat,lng, t):
		p = geometry.Point(float(lng),float(lat))
		for e in self.data[t]:
			if self.data[t][e]["polygon"].touches(p) or self.data[t][e]["polygon"].contains(p):
				return self.data[t][e]
		return False