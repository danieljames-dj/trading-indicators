def custom_ma(source, prev, alpha):
  custom_ma = alpha * source[-1] + (1 - alpha) * prev[-1]
  return custom_ma

def sma(source, length):
  sma_value = 0
  for value in source[-length:]:
    sma_value += value
  sma_value /= length
  return sma_value

def ema(source, prev, length, smoothing = 2):
  if len(prev) == 0:
    if len(source) < length:
      return None
    else:
      return sma(source, length)
  else:
    alpha = smoothing/(length+1)
    return custom_ma(source, prev, alpha)

def rma(source, prev, length):
  if len(prev) == 0:
    if len(source) < length:
      return None
    else:
      return sma(source, length)
  else:
    alpha = 1/length
    return custom_ma(source, prev, alpha)