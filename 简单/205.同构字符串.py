

class Solution:
	def isIsomorphic(self, s, t):
		return [*map(s.index, s)] == [*map(t.index, t)]