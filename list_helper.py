"""
    列表助手模块
"""

class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target,func_condition):
        """
            通用的查找多个条件的单个元素方法
        :param list_target:目标列表
        :param function_condition:查找条件
        :return:多个元素
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target,function_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target:目标列表
        :param function_condition:查找条件
        :return:单个元素
        """
        for item in list_target :
            if function_condition(item):
                return item

    @staticmethod
    def get_count(list_target,function_condition):
        """
            通用查找元素个数的方法
        :param list_target:目标列表
        :param function_condition:查找元素
        :return: --->int次数
        """
        count_value = 0
        for item in list_target:
            if function_condition(item):
                count_value += 1
        return  count_value

    @staticmethod
    def is_exists(list_target, func_condition):
        """

        :param list_target: 查询列表
        :param func_condition: 判断条件
        :return: bool值,True表示存在,False表示不存在
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def get_resulte(list_target,func_handle):
        """
            通用的获取数值总和的方法
        :param list_target: 目标列表
        :param func_handle: 单个值
        :return: 生成器
        """
        sum_value = 0
        for item in list_target:
            sum_value += func_handle(item)
        return sum_value

    @staticmethod
    def output(list_target,func_handle):
        for item in list_target:
            yield func_handle(item)

    @staticmethod
    def max(list_target,handle):
        """
           通用获取最大元素的方法
        :param list_target:目标列表
        :param handle: 需要搜索的处理逻辑,函数类型
        :return: 生成器
        """
        max_value = list_target[0]
        for i in range(1,len(list_target)):
            if  handle(max_value) < handle(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def ord_by01(list_target,handle):
        """
            通用的升序排列方法
        :param list_target:需要排序的逻辑
        :param handle: 需要搜多的处理逻辑,函数类型
        :return:
        """
        for r in range(len(list_target)-1):
            for c in range(r+1,len(list_target)):
                if handle(list_target[r]) > handle(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]

