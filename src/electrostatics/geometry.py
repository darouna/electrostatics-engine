def set_plates(V, mask, v_high, v_low=0):
    mask[:,0] = True
    mask[:,-1] = True
    V[:,0] = v_high
    V[:,-1] = v_low
    return V, mask