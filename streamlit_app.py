
import numpy as np
import math


import pickle
import streamlit as st

#matplotlib.use('TkAgg')
st.title('Bentonite Co  &  Albrehta Co')
st.title('HDD BENTONITE ML-TESTER')
#bent = st.checkbox('base bentonite')
col1, col2 = st.columns(2)
bent = col1.checkbox('base bentonite')
vis = col2.checkbox('low viscosity')
#pac = col1.number_input('PAC', min_value = 2.0, value = 4.0, step = 0.1)
#flom = col1.number_input('Flomin', min_value = 0.2, value = 0.4, step = 0.01)
#pac = float(input('Кнцентрация PAC: '))
#flom = float(input('Концентрация Flomin: '))
if bent or vis:
    rates = {'3':3}
else:
    rates = {'2':2, '3':3}
conc = float(col1.selectbox('Концентрация суспензии', list(rates)))
#conc = float(input('Концентрация суспензии: '))
f600 = col1.slider('FANN_600', 10, 85, 75)
#f600 = float(input('f600: '))
f300 = col1.slider('FANN_300', 5, 65, 60)
f3 = col2.slider('FANN_3', 1, 25, 24)
#f3 = float(input('f3: '))
gel_1 = col2.slider('GEL_1min, psf', 2, 45, 43)
#gel_1 = float(input('GEL_1: '))
gel_10 = col2.slider('GEL_10min, psf', 3, 70, 67)
#gel = float(input('GEL_10: '))
tics = gel_10/gel_1
pv = f600-f300
yp = f300-pv
n = math.log10(f600/f300)/math.log10(2)
K = f300/(300**n)
LSRV = 1000*n*K*0.0511**(n-1)

#def dff():
if st.button('TEST'):
    if bent and vis == False:
        if f600 < 17:
            col1.error(f'FANN_600: {f600:,.1f}')
        elif f600 >= 17 and f600 <= 21:
            col1.warning(f'FANN_600: {f600:,.1f}')
        else:
            col1.success(f'FANN_600: {f600:,.1f}')

        if f3 < 6:
            col1.error(f'FANN_3: {f3:,.1f}')
        elif f3 >= 6 and f3 <= 14:
            col1.warning(f'FANN_3: {f3:,.1f}')
        else:
            col1.success(f'FANN_3: {f3:,.1f}')
        
        if tics <= 1.5:
            col1.error(f'Коэф тиксотропии TS: {tics:,.1f}')
        elif tics > 1.5 and tics <= 1.8:
            col1.warning(f'Коэф тиксотропии TS: {tics:,.1f}')
        else:
            col1.success(f'Коэф тиксотропии TS: {tics:,.1f}')

        if pv >=6:
            col1.error(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
        elif pv > 3 and pv < 6:
            col1.warning(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
        else:
            col1.success(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')

        if gel_10 <= 34:
            col1.error(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
        elif gel_10 > 34 and gel_10 <= 42:
            col1.warning(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
        else:
            col1.success(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')

        if yp >= 15:
            col2.success(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
        elif yp >= 10 and yp < 15:
            col2.warning(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
        else:
            col2.error(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')

        if n > 0.5:
            col2.error(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
        elif n <= 0.5 and n > 0.3:
            col2.warning(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
        else:
            col2.success(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')

        if K >= 4:
            col2.success(f'Коэф консистенции K: {f300/(300**n):,.1f}')
        elif K >= 1.5 and K < 4:
            col2.warning(f'Коэф консистенции K: {f300/(300**n):,.1f}')
        else:
            col2.error(f'Коэф консистенции K: {f300/(300**n):,.1f}')

        if LSRV > 10000:
            col2.success(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
        elif LSRV >= 4000 and LSRV <= 10000:
            col2.warning(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
        else:
            col2.error(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')

    elif vis or (vis and bent):
        if f600 <= 34:
            col1.error(f'FANN_600: {f600:,.1f}')
        elif f600 > 34 and f600 <= 42:
            col1.warning(f'FANN_600: {f600:,.1f}')
        else:
            col1.success(f'FANN_600: {f600:,.1f}')
        
        if tics <= 1.25:
            col1.error(f'Коэф тиксотропии TS: {tics:,.1f}')
        elif tics > 1.25 and tics <= 1.4:
            col1.warning(f'Коэф тиксотропии TS: {tics:,.1f}')
        else:
            col1.success(f'Коэф тиксотропии TS: {tics:,.1f}')

        if f3 < 9:
            col1.error(f'FANN_3: {f3:,.1f}')
        elif f3 >= 9 and f3 < 14:
            col1.warning(f'FANN_3: {f3:,.1f}')
        else:
            col1.success(f'FANN_3: {f3:,.1f}')
    
        if pv >= 14:
            col1.error(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
        elif pv >= 9 and pv < 14:
            col1.warning(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
        else:
            col1.success(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')

        if gel_10 <= 22:
            col1.error(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
        elif gel_10 > 22 and gel_10 <= 28:
            col1.warning(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
        elif gel_10 > 28 and gel_10 <= 38:
            col1.success(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
        else:
            col1.error(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')

        if yp > 25:
            col2.success(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
        elif yp >= 18 and yp <= 25:
            col2.warning(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
        else:
            col2.error(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')

        if n > 0.6:
            col2.error(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
        elif n <= 0.6 and n > 0.45:
            col2.warning(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
        else:
            col2.success(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')

        if K >= 3:
            col2.success(f'Коэф консистенции K: {f300/(300**n):,.2f}')
        elif K >= 1.5 and K < 3:
            col2.warning(f'Коэф консистенции K: {f300/(300**n):,.2f}')
        else:
            col2.error(f'Коэф консистенции K: {f300/(300**n):,.2f}')

        if LSRV > 6000:
            col2.success(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
        elif LSRV >= 3500 and LSRV <= 6000:
            col2.warning(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
        else:
            col2.error(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')     
    
    else:
    
        if conc == 2:
            if f600 <= 26:
                col1.error(f'FANN_600: {f600:,.1f}')
            elif f600 > 26 and f600 <= 30:
                col1.warning(f'FANN_600: {f600:,.1f}')
            else:
                col1.success(f'FANN_600: {f600:,.1f}')
            
            if tics <= 1.3:
                col1.error(f'Коэф тиксотропии TS: {tics:,.1f}')
            elif tics > 1.3 and tics <= 1.6:
                col1.warning(f'Коэф тиксотропии TS: {tics:,.1f}')
            else:
                col1.success(f'Коэф тиксотропии TS: {tics:,.1f}')

            if f3 < 3:
                col1.error(f'FANN_3: {f3:,.1f}')
            elif f3 >= 3 and f3 <= 4:
                col1.warning(f'FANN_3: {f3:,.1f}')
            else:
                col1.success(f'FANN_3: {f3:,.1f}')
        
            if pv >13:
                col1.error(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
            elif pv >= 10 and pv <= 13:
                col1.warning(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
            else:
                col1.success(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')

            if gel_10 < 13:
                col1.error(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
            elif gel_10 >= 13 and gel_10 <= 16:
                col1.warning(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
            elif gel_10 > 16 and gel_10 <= 23:
                col1.success(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
            else:
                col1.error(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')

            if yp >= 13:
                col2.success(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
            elif yp >= 8 and yp < 13:
                col2.warning(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
            else:
                col2.error(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')

            if n > 0.7:
                col2.error(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
            elif n <= 0.7 and n > 0.5:
                col2.warning(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
            else:
                col2.success(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')

            if K >= 1.5:
                col2.success(f'Коэф консистенции K: {f300/(300**n):,.2f}')
            elif K >= 0.5 and K < 1.5:
                col2.warning(f'Коэф консистенции K: {f300/(300**n):,.2f}')
            else:
                col2.error(f'Коэф консистенции K: {f300/(300**n):,.2f}')

            if LSRV > 3000:
                col2.success(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
            elif LSRV >= 800 and LSRV <= 3000:
                col2.warning(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
            else:
                col2.error(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
        else:
            if f600 <= 45:
                col1.error(f'FANN_600: {f600:,.1f}')
            elif f600 > 45 and f600 <= 48:
                col1.warning(f'FANN_600: {f600:,.1f}')
            else:
                col1.success(f'FANN_600: {f600:,.1f}')
            
            if tics <= 1.3:
                col1.error(f'Коэф тиксотропии TS: {tics:,.1f}')
            elif tics > 1.3 and tics <= 1.6:
                col1.warning(f'Коэф тиксотропии TS: {tics:,.1f}')
            else:
                col1.success(f'Коэф тиксотропии TS: {tics:,.1f}')

            if f3 < 9:
                col1.error(f'FANN_3: {f3:,.1f}')
            elif f3 >= 9 and f3 < 15:
                col1.warning(f'FANN_3: {f3:,.1f}')
            else:
                col1.success(f'FANN_3: {f3:,.1f}')
        
            if pv >= 18:
                col1.error(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
            elif pv >= 14 and pv < 18:
                col1.warning(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')
            else:
                col1.success(f'Пластическая вязкость PV: {f600-f300:,.1f} мПа*с')

            if gel_10 < 32:
                col1.error(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
            elif gel_10 >= 32 and gel_10 <= 38:
                col1.warning(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
            elif gel_10 > 38 and gel_10 <= 46:
                col1.success(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')
            else:
                col1.error(f'Статическое напряжение сдвига GEL_10min: {gel_10:,.1f} psf ({gel_10*4.8:,.1f}) дПа')

            if yp > 25:
                col2.success(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
            elif yp >= 18 and yp <= 25:
                col2.warning(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')
            else:
                col2.error(f'Динамическое напряжение сдвига YP: {yp:,.2f} psf ({yp*4.8:,.1f}) дПа')

            if n > 0.6:
                col2.error(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
            elif n <= 0.6 and n > 0.45:
                col2.warning(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')
            else:
                col2.success(f'Коэф псевдопластичности n: {math.log10(f600/f300)/math.log10(2):,.1f}')

            if K >= 3:
                col2.success(f'Коэф консистенции K: {f300/(300**n):,.2f}')
            elif K >= 1.5 and K < 3:
                col2.warning(f'Коэф консистенции K: {f300/(300**n):,.2f}')
            else:
                col2.error(f'Коэф консистенции K: {f300/(300**n):,.2f}')

            if LSRV > 6000:
                col2.success(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
            elif LSRV >= 3500 and LSRV <= 6000:
                col2.warning(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
            else:
                col2.error(f'Вязкость при низкой скорости сдвига LSRV: {1000*n*K*0.0511**(n-1):,.1f} мПа*с')
      

