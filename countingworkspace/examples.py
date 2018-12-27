import numpy as np

NCATEGORIES = 29
NPROCESS = 4
LUMI = 79.9  # /fb
EXPECTED_BKG_CAT = np.array(
    [
        13000,
        46000,
        19000,
        6900,
        640,
        80,
        7700,
        4100,
        690,
        61,
        280,
        35,
        690,
        320,
        470,
        110,
        610,
        9.8,
        6.5,
        95,
        5.3,
        2.6,
        55,
        33,
        8.2,
        1.4,
        4.7,
        4.9,
        2.2,
    ]
)

XSECFID_X_BR_PRODUCTION_MODES = np.array([101.5, 7.99, 4.53, 1.33])  # fb for |y| < 2.5
NTRUE = XSECFID_X_BR_PRODUCTION_MODES * LUMI

EFFICIENCIES_CAT_PRODUCTIONMODE = np.array(
    [
        [8.44062260e-02, 1.16227364e-02, 1.61568737e-02, 2.21471081e-04],
        [1.48438055e-01, 2.25251625e-02, 3.34504964e-02, 5.16342535e-04],
        [7.03025018e-02, 5.48094329e-02, 4.55980273e-02, 1.79441904e-03],
        [3.40335068e-02, 6.04452130e-02, 4.00562096e-02, 1.94788412e-03],
        [6.44775164e-03, 1.91181543e-02, 1.21023871e-02, 8.37050522e-04],
        [1.63443080e-03, 5.66171925e-03, 3.61359292e-03, 3.15114144e-04],
        [1.82444815e-02, 2.60907985e-02, 3.63153945e-02, 2.22397786e-02],
        [1.47371599e-02, 2.95007997e-02, 3.28717953e-02, 2.28440668e-02],
        [6.01598386e-03, 1.28199282e-02, 1.49638079e-02, 9.39107884e-03],
        [1.47773364e-03, 2.51609796e-03, 4.10525618e-03, 3.15075368e-03],
        [1.75964497e-03, 4.19176733e-02, 7.92689640e-04, 6.44170371e-04],
        [4.57390154e-04, 3.99063912e-02, 1.69339063e-04, 4.46022196e-04],
        [3.36384473e-03, 1.37667073e-02, 4.34326254e-03, 4.32904318e-03],
        [2.73503896e-03, 3.38346337e-02, 3.38377223e-03, 7.51175640e-03],
        [2.84039922e-03, 2.82836547e-03, 2.45596744e-02, 4.92609509e-03],
        [1.64421768e-03, 1.42465816e-03, 2.98544652e-02, 3.23415637e-03],
        [2.96175128e-03, 1.81893331e-02, 1.36502193e-02, 1.64941219e-02],
        [2.85601233e-05, 2.39438347e-05, 3.26981834e-03, 8.72434853e-05],
        [4.00076269e-06, 5.98595867e-06, 6.99679950e-03, 1.37593074e-03],
        [1.56610555e-04, 1.88557698e-04, 2.67914297e-02, 1.25997600e-02],
        [0.00000000e00, 2.99297934e-06, 7.08503133e-03, 4.87655802e-03],
        [0.00000000e00, 0.00000000e00, 4.97653608e-03, 2.24815038e-04],
        [2.06116500e-04, 3.83101355e-04, 2.77824215e-03, 3.74897217e-02],
        [1.14597907e-04, 1.64613864e-04, 1.71443422e-03, 5.48209404e-02],
        [3.43732284e-05, 4.78876694e-05, 5.70120190e-04, 3.87107900e-02],
        [1.77763028e-05, 2.59391543e-05, 3.94666075e-04, 4.71152975e-02],
        [1.10770251e-06, 1.99531956e-06, 3.11618505e-04, 1.08863584e-02],
        [0.00000000e00, 9.97659779e-07, 2.27969899e-04, 2.62151681e-02],
        [0.00000000e00, 0.00000000e00, 1.34483704e-04, 5.06637263e-02],
    ]
)

EFFICIENCIES = EFFICIENCIES_CAT_PRODUCTIONMODE * 0.9

NAMES_PROC = ['ggF', 'VBF', 'VH', 'TOP']