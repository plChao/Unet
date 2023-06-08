import numpy as np
import cv2

def drop_outlyers_cont(contours, CEJ_mask, vis_process_mask, img_size):
    choose_contours = []
    y_cord = np.nonzero(CEJ_mask)[0]
    y_mean, y_std = np.mean(y_cord), np.std(y_cord)
    cv2.line(vis_process_mask, (0, int(y_mean + 2*y_std)), (img_size, int(y_mean + 2*y_std)), (0, 0, 255), 2)
    cv2.line(vis_process_mask, (0, int(y_mean - 2*y_std)), (img_size, int(y_mean - 2*y_std)), (0, 0, 255), 2)
    for cont in contours:
        flag = True
        for pt in cont[0]:
            if pt[1] > y_mean + 2*y_std or pt[1] < y_mean - 2*y_std:
                cv2.drawContours(vis_process_mask, [cont], -1, (255, 0, 0), cv2.FILLED)
                flag = False
                break
        if flag:
            choose_contours.append(cont)
    return choose_contours