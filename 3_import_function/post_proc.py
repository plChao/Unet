import numpy as np
import cv2

def drop_outlyers_cont(contours, CEJ_mask, vis_process_mask, img_size, thresh=400):
    choose_contours = []
    y_cord = np.nonzero(CEJ_mask)[0]
    y_mean, y_std = np.mean(y_cord), np.std(y_cord)
    cv2.line(vis_process_mask, (0, int(y_mean + thresh)), (img_size, int(y_mean + thresh)), (0, 0, 255), 2)
    cv2.line(vis_process_mask, (0, int(y_mean - thresh)), (img_size, int(y_mean - thresh)), (0, 0, 255), 2)
    for cont in contours:
        cnt = 0
        s_cont = np.squeeze(cont, axis=1)
        for pt in s_cont:
            if pt[1] > y_mean + thresh or pt[1] < y_mean - thresh:
                cnt += 1
        if cnt / len(s_cont) <= 0.5:
            choose_contours.append(cont)
        else:
            cv2.drawContours(vis_process_mask, [cont], -1, (0, 0, 255), cv2.FILLED)
    return choose_contours