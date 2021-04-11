# encoding: utf-8
def compute_IOU(box1, box2):
    """
    计算两个矩形框的交并比
    :param box1: (xmin, ymin, xmax, ymax)  (xmin, ymin)代表矩形左下的顶点, (xmax, ymax)代表矩形右上的顶点
    :param box2: (xmin, ymin, xmax, ymax)
    :return: IOU
    """
    # 找到中间的 Cross Box 的坐标信息
    cross_box_xmin = max(box1[0], box2[0])
    cross_box_ymin = max(box1[1], box2[1])
    cross_box_xmax = min(box1[2], box2[2])
    cross_box_ymax = min(box1[3], box2[3])

    # 两个矩形没有相交的情况
    if cross_box_xmin >= cross_box_xmax or cross_box_ymax <= cross_box_ymin:
        return 0.0
    else:
        # 计算两个矩形的面积
        S1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        S2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
        S_cross = (cross_box_xmax - cross_box_xmin) * (cross_box_ymax - cross_box_ymin)
        return S_cross / (S1 + S2 - S_cross)


if __name__ == "__main__":
    # example 1
    box1 = [100, 100, 200, 200]
    box2 = [150, 150, 250, 250]
    print(compute_IOU(box1, box2))

    # example 2
    box1 = [0, 5, 5, 10]
    box2 = [3, 2, 8, 7]
    print(compute_IOU(box1, box2))
