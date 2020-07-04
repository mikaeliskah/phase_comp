
# simple Kalman-Filter module

''' variable description:
meas_val = current measurement value
est_prev = previous estimate
err_est_prev = error of previous estimate
err_meas = measurement error
'''


def filter(meas_val, est_prev, err_est_prev, err_meas):
    # calculate kalman gain
    kg = err_est_prev / (err_est_prev+err_meas)
    # calculate estimate
    est = est_prev + (kg * (meas_val-est_prev))
    # calculate error
    err_est = (1-kg)*err_est_prev
    return est, err_est
