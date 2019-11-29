"""
示例 1：

输入：date = "2019-01-09"
输出：9
示例 2：

输入：date = "2019-02-10"
输出：41
示例 3：

输入：date = "2003-03-01"
输出：60
示例 4：

输入：date = "2004-03-01"
输出：61
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/day-of-the-year
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
	def dayOfYear(self, date: str) -> int:
		year, month, day = [int(i) for i in date.split("-")]
		monthnums_list = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		# 判断是否是闰年
		if year % 4 == 0 and year % 100 != 0:
			monthnums_list[1] = 29
		elif year % 400 == 0:
			monthnums_list[1] = 29
		else:
			monthnums_list[1] = 28
		return sum(monthnums_list[:month - 1]) + day





