# -*- coding: utf-8 -*-
"""
Gives water properties in various physical conditions.

@author: Adapted from Louis Lamarche by Tanguy Lunel
"""
# flake8: noqa: C901

import numpy as np


class Switch(object):
    def __init__(self,  value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self,  *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


# TODO: rewrite this function for more readibility, and remove the issue
# noticed in 'N.B.:'
def water_prop(name,  T):
    """
    Function giving water property requested.

    Parameters
    ----------
    name: str
        Options are :
            'temp',
            'pres',
            'vf': fluid specific volume [m3/kg],
            'rhof': fluid density [kg/m3] - reverse of vf,
            'vg',
            'hfg',
            'Cpf',
            'Cpg',
            'muf': dynamic viscosity,
            'mug',
            'nug': cinematic viscosity of vapor (gas),
            'nuf': cinematic viscosity of fluid water (uses 'muf' and 'rhof')
            'kf',
            'kg',
            'Prf',
            'Prg',
            'st',
            'betaf'
    T: float,
        Temperature at which the property is wanted
        N.B.:
            if name == 'temp', T must be replaced by pression [in bar]

    Returns
    -------
    * float
    """

    properties_table = np.array([
            [273.130000, 0.006110, 1.000000, 206.300000, 2502.000000,
             4.217000, 1.854000, 1750.000000, 8.020000, 569.000000,
             18.200000, 12.990000, 0.815000, 75.500000, -68.050000],
            [275.000000, 0.006970, 1.000000, 181.700000, 2497.000000,
             4.211000, 1.855000, 1652.000000, 8.090000, 574.000000,
             18.300000, 12.220000, 0.817000, 75.300000, -32.740000],
            [280.000000, 0.009900, 1.000000, 130.400000, 2485.000000,
             4.198000, 1.858000, 1422.000000, 8.290000, 582.000000,
             18.600000, 10.260000, 0.825000, 74.800000, 46.040000],
            [285.000000, 0.013870, 1.000000, 99.400000, 2473.000000,
             4.189000, 1.861000, 1225.000000, 8.490000, 590.000000,
             18.900000, 8.810000, 0.833000, 74.300000, 114.100000],
            [290.000000, 0.019170, 1.001000, 69.700000, 2461.000000,
             4.184000, 1.864000, 1080.000000, 8.690000, 598.000000,
             19.300000, 7.560000, 0.841000, 73.700000, 174.000000],
            [295.000000, 0.026170, 1.002000, 51.940000, 2449.000000,
             4.181000, 1.868000, 959.000000, 8.890000, 606.000000,
             19.500000, 6.620000, 0.849000, 72.700000, 227.500000],
            [300.000000, 0.035310, 1.003000, 39.130000, 2438.000000,
             4.179000, 1.872000, 855.000000, 9.090000, 613.000000,
             19.600000, 5.830000, 0.857000, 71.700000, 276.100000],
            [305.000000, 0.047120, 1.005000, 29.740000, 2426.000000,
             4.178000, 1.877000, 769.000000, 9.290000, 620.000000,
             20.100000, 5.200000, 0.865000, 70.900000, 320.600000],
            [310.000000, 0.062210, 1.007000, 22.930000, 2414.000000,
             4.178000, 1.882000, 695.000000, 9.490000, 628.000000,
             20.400000, 4.620000, 0.873000, 70.000000, 361.900000],
            [315.000000, 0.081320, 1.009000, 17.820000, 2402.000000,
             4.179000, 1.888000, 631.000000, 9.690000, 634.000000,
             20.700000, 4.160000, 0.883000, 69.200000, 400.400000],
            [320.000000, 0.105300, 1.011000, 13.980000, 2390.000000,
             4.180000, 1.895000, 577.000000, 9.890000, 640.000000,
             21.000000, 3.770000, 0.894000, 68.300000, 436.700000],
            [325.000000, 0.135100, 1.013000, 11.060000, 2378.000000,
             4.182000, 1.903000, 528.000000, 10.090000, 645.000000,
             21.300000, 3.420000, 0.901000, 67.500000, 471.200000],
            [330.000000, 0.171900, 1.016000, 8.820000, 2366.000000,
             4.194000, 1.911000, 489.000000, 10.290000, 650.000000,
             21.700000, 3.150000, 0.908000, 66.600000, 504.000000],
            [335.000000, 0.216700, 1.018000, 7.090000, 2354.000000,
             4.186000, 1.920000, 453.000000, 10.490000, 656.000000,
             22.000000, 2.880000, 0.916000, 65.800000, 535.500000],
            [340.000000, 0.271300, 1.021000, 5.740000, 2342.000000,
             4.188000, 1.930000, 420.000000, 10.690000, 660.000000,
             22.300000, 2.660000, 0.925000, 64.900000, 566.000000],
            [345.000000, 0.337200, 1.024000, 4.683000, 2329.000000,
             4.191000, 1.941000, 389.000000, 10.890000, 668.000000,
             22.600000, 2.450000, 0.933000, 64.100000, 595.400000],
            [350.000000, 0.416300, 1.027000, 3.846000, 2317.000000,
             4.195000, 1.954000, 365.000000, 11.090000, 668.000000,
             23.000000, 2.290000, 0.942000, 63.200000, 624.200000],
            [355.000000, 0.510000, 1.030000, 3.180000, 2304.000000,
             4.199000, 1.968000, 343.000000, 11.290000, 671.000000,
             23.300000, 2.140000, 0.951000, 62.300000, 652.300000],
            [360.000000, 0.620900, 1.034000, 2.645000, 2291.000000,
             4.203000, 1.983000, 324.000000, 11.490000, 674.000000,
             23.700000, 2.020000, 0.960000, 61.400000, 697.900000],
            [365.000000, 0.751400, 1.038000, 2.212000, 2278.000000,
             4.209000, 1.999000, 306.000000, 11.690000, 677.000000,
             24.100000, 1.910000, 0.969000, 60.500000, 707.100000],
            [370.000000, 0.904000, 1.041000, 1.961000, 2265.000000,
             4.214000, 2.017000, 289.000000, 11.890000, 679.000000,
             24.500000, 1.800000, 0.978000, 59.500000, 728.700000],
            [373.150000, 1.013300, 1.044000, 1.679000, 2257.000000,
             4.217000, 2.029000, 279.000000, 12.020000, 680.000000,
             24.800000, 1.760000, 0.994000, 58.900000, 750.100000],
            [375.000000, 1.081500, 1.045000, 1.574000, 2252.000000,
             4.220000, 2.036000, 274.000000, 12.090000, 681.000000,
             24.900000, 1.700000, 0.987000, 58.600000, 761.000000],
            [380.000000, 1.286900, 1.049000, 1.337000, 2239.000000,
             4.226000, 2.057000, 260.000000, 12.290000, 683.000000,
             25.400000, 1.610000, 0.999000, 57.600000, 798.000000],
            [385.000000, 1.523300, 1.053000, 1.142000, 2225.000000,
             4.232000, 2.080000, 248.000000, 12.490000, 685.000000,
             25.800000, 1.530000, 1.004000, 56.600000, 814.000000],
            [390.000000, 1.794000, 1.058000, 0.980000, 2212.000000,
             4.239000, 2.104000, 237.000000, 12.690000, 686.000000,
             26.300000, 1.470000, 1.013000, 55.600000, 841.000000],
            [400.000000, 2.455000, 1.067000, 0.731000, 2183.000000,
             4.256000, 2.158000, 217.000000, 13.050000, 688.000000,
             27.200000, 1.340000, 1.033000, 53.600000, 896.000000],
            [410.000000, 3.302000, 1.077000, 0.553000, 2153.000000,
             4.278000, 2.221000, 200.000000, 13.420000, 688.000000,
             28.200000, 1.240000, 1.054000, 51.500000, 952.000000],
            [420.000000, 4.370000, 1.088000, 0.425000, 2123.000000,
             4.302000, 2.291000, 185.000000, 13.790000, 688.000000,
             29.800000, 1.160000, 1.075000, 49.400000, 1010.000000],
            [430.000000, 5.699000, 1.099000, 0.331000, 2091.000000,
             4.331000, 2.369000, 173.000000, 14.140000, 685.000000,
             30.400000, 1.090000, 1.100000, 47.200000, 0.000000],
            [440.000000, 7.333000, 1.110000, 0.261000, 2059.000000,
             4.360000, 2.460000, 162.000000, 14.500000, 682.000000,
             31.700000, 1.040000, 1.120000, 45.100000, 0.000000],
            [450.000000, 9.319000, 1.123000, 0.208000, 2024.000000,
             4.400000, 2.560000, 152.000000, 14.850000, 678.000000,
             33.100000, 0.990000, 1.140000, 42.900000, 0.000000],
            [460.000000, 11.710000, 1.137000, 0.167000, 1989.000000,
             4.440000, 2.680000, 143.000000, 15.190000, 673.000000,
             34.600000, 0.950000, 1.170000, 40.700000, 0.000000],
            [470.000000, 14.550000, 1.152000, 0.136000, 1951.000000,
             4.480000, 2.790000, 136.000000, 15.540000, 667.000000,
             36.300000, 0.920000, 1.200000, 38.500000, 0.000000],
            [480.000000, 17.900000, 1.167000, 0.111000, 1912.000000,
             4.530000, 2.940000, 129.000000, 15.880000, 660.000000,
             38.100000, 0.890000, 1.230000, 36.200000, 0.000000],
            [490.000000, 21.830000, 1.184000, 0.092200, 1870.000000,
             4.590000, 3.100000, 124.000000, 16.230000, 651.000000,
             40.100000, 0.870000, 1.250000, 33.900000, 0.000000],
            [500.000000, 26.400000, 1.203000, 0.076600, 1825.000000,
             4.660000, 3.270000, 118.000000, 16.590000, 642.000000,
             42.300000, 0.860000, 1.280000, 31.600000, 0.000000],
            [510.000000, 31.660000, 1.222000, 0.063100, 1779.000000,
             4.740000, 3.470000, 113.000000, 16.950000, 631.000000,
             44.700000, 0.850000, 1.310000, 29.300000, 0.000000],
            [520.000000, 37.700000, 1.244000, 0.052500, 1730.000000,
             4.840000, 3.700000, 108.000000, 17.330000, 621.000000,
             47.500000, 0.840000, 1.350000, 26.900000, 0.000000],
            [530.000000, 44.580000, 1.268000, 0.044500, 1679.000000,
             4.950000, 3.960000, 104.000000, 17.720000, 608.000000,
             50.600000, 0.850000, 1.390000, 24.500000, 0.000000],
            [540.000000, 52.380000, 1.294000, 0.037500, 1622.000000,
             5.080000, 4.270000, 101.000000, 18.100000, 594.000000,
             54.000000, 0.860000, 1.430000, 22.100000, 0.000000],
            [550.000000, 61.190000, 1.323000, 0.031700, 1564.000000,
             5.240000, 4.640000, 97.000000, 18.600000, 580.000000,
             58.300000, 0.870000, 1.470000, 19.700000, 0.000000],
            [560.000000, 71.080000, 1.355000, 0.026900, 1499.000000,
             5.430000, 5.090000, 94.000000, 19.100000, 563.000000,
             63.700000, 0.900000, 1.520000, 17.300000, 0.000000],
            [570.000000, 82.160000, 1.392000, 0.022800, 1429.000000,
             5.680000, 5.670000, 91.000000, 19.700000, 548.000000,
             76.700000, 0.940000, 1.590000, 15.000000, 0.000000],
            [580.000000, 94.510000, 1.433000, 0.019300, 1353.000000,
             6.000000, 6.400000, 88.000000, 20.400000, 528.000000,
             76.700000, 0.990000, 1.680000, 12.800000, 0.000000],
            [590.000000, 108.300000, 1.482000, 0.016300, 1274.000000,
             6.410000, 7.350000, 84.000000, 21.500000, 513.000000,
             84.100000, 1.050000, 1.840000, 10.500000, 0.000000],
            [600.000000, 123.500000, 1.541000, 0.013700, 1176.000000,
             7.000000, 8.750000, 81.000000, 22.700000, 497.000000,
             92.900000, 1.140000, 2.150000, 8.400000, 0.000000],
            [610.000000, 137.300000, 1.612000, 0.011500, 1068.000000,
             7.850000, 11.100000, 77.000000, 24.100000, 467.000000,
             103.000000, 1.300000, 2.600000, 6.300000, 0.000000],
            [620.000000, 159.100000, 1.705000, 0.009400, 941.000000,
             9.350000, 15.400000, 72.000000, 25.900000, 444.000000,
             114.000000, 1.520000, 3.460000, 4.500000, 0.000000],
            [625.000000, 169.100000, 1.778000, 0.008500, 858.000000,
             10.600000, 18.300000, 70.000000, 27.000000, 430.000000,
             121.000000, 1.650000, 4.200000, 3.500000, 0.000000],
            [630.000000, 179.700000, 1.856000, 0.007500, 781.000000,
             12.600000, 22.100000, 67.000000, 28.000000, 412.000000,
             130.000000, 2.000000, 4.800000, 2.600000, 0.000000],
            [635.000000, 190.900000, 1.935000, 0.006600, 683.000000,
             16.400000, 27.600000, 64.000000, 30.000000, 392.000000,
             141.000000, 2.700000, 6.000000, 1.500000, 0.000000],
            [640.000000, 202.700000, 2.075000, 0.005700, 560.000000,
             26.000000, 42.000000, 59.000000, 32.000000, 367.000000,
             155.000000, 4.200000, 9.600000, 0.800000, 0.000000],
            [645.000000, 215.200000, 2.351000, 0.004500, 361.000000,
             90.000000, 0.000000, 54.000000, 37.000000, 331.000000,
             178.000000, 12.000000, 26.000000, 0.100000, 0.000000],
            [647.300000, 221.200000, 3.170000, 0.003200, 0.000000,
             100000000000000000000.000000, 100000000000000000000.000000,
             45.000000, 45.000000, 238.000000, 238.000000,
             100000000000000000000.000000, 100000000000000000000.000000,
             0.000000, 0.000000]])

    label = ['temp', 'pres', 'vf', 'vg', 'hfg', 'Cpf', 'Cpg', 'muf', 'mug',
             'kf', 'kg', 'Prf', 'Prg', 'st', 'betaf']

    for case in Switch(name):
        if case('temp'):
            y = properties_table[:, 0]
            x = properties_table[:, 1]
            pmin = x[0]
            pmax = x[x.size-1]
            if T < pmin or T > pmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            break
        if case('muf', 'mug'):
            i = label.index(name)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            p = p*10**-6
            break
        if case('nuf'):
            name1 = 'muf'
            i = label.index(name1)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p1 = np.interp(T, x,  y)
            name2 = 'vf'
            i = label.index(name2)
            y = properties_table[:, i]
            p2 = np.interp(T, x,  y)
            p = p1*p2*10**-9
            break
        if case('nug'):
            name1 = 'mug'
            i = label.index(name1)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p1 = np.interp(T, x,  y)
            name2 = 'vg'
            i = label.index(name2)
            y = properties_table[:, i]
            p2 = np.interp(T, x,  y)
            p = p1*p2*10**-6
            break
        if case('alg'):
            name1 = 'kg'
            i = label.index(name1)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p1 = np.interp(T, x,  y)
            name2 = 'vg'
            i = label.index(name2)
            y = properties_table[:, i]
            p2 = np.interp(T, x,  y)
            name3 = 'Cpg'
            i = label.index(name2)
            y = properties_table[:, i]
            p3 = np.interp(T, x,  y)
            p = (p1*p2/p3)*10**-6
            break
        if case('alf'):
            name1 = 'kf'
            i = label.index(name1)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p1 = np.interp(T, x,  y)
            name2 = 'vf'
            i = label.index(name2)
            y = properties_table[:, i]
            p2 = np.interp(T, x,  y)
            name3 = 'Cpf'
            i = label.index(name3)
            y = properties_table[:, i]
            p3 = np.interp(T, x,  y)
            p = (p1*p2/p3)*10**-9
            break
        if case('kf', 'kg', 'st'):
            i = label.index(name)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            p = p*10**-3
            break
        if case('Cpf', 'Cpg', 'hfg'):
            i = label.index(name)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            p = p*10**3
            break
        if case('vf'):
            i = label.index(name)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            p = p*10**-3
            break
        if case('rhof'):
            name2 = 'vf'
            i = label.index(name2)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            p = 1000.0/p
            break
        if case('rhog'):
            name2 = 'vg'
            i = label.index(name2)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            p = 1000.0/p
            break
        if case('betaf'):
            i = label.index(name)
            y = properties_table[:, i]
            x = properties_table[:, 0]
            Tmin = x[0]
            Tmax = x[x.size-1]
            if T < Tmin or T > Tmax:
                print('Warning: T is out of the table: data extrapolated')
            p = np.interp(T, x,  y)
            p = p*10**-6
            break
        i = label.index(name)
        y = properties_table[:, i]
        x = properties_table[:, 0]
        Tmin = x[0]
        Tmax = x[x.size-1]
        if T < Tmin or T > Tmax:
            print('Warning: T is out of the table: data extrapolated')
        p = np.interp(T, x,  y)
    return p


def vap_p(Tk):
    """Compute vapor pressure of water.
    Tk is given in Kelvin"""
    T = Tk - 273.15
    p = 6.11*10**(7.5*T/(237.3+T))
    p = p*100.0
    return p
