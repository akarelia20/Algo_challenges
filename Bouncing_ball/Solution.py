def bouncing_ball(h, bounce, window):
    if h > window and h > 0 and (bounce > 0 and bounce < 1):
        count= 0
        bounce_height = h * bounce
        while h > window:
            count += 1
            bounce_height = h * bounce
            h = bounce_height
            if bounce_height > window:
                count+=1
        return count
    else:
        return -1