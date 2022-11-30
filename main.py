import numpy as np


def calc_weighted_budget(T_B, index, T_Deltas, Cap_R, K_R):
    if (T_B - Cap_R[index]) > 0:
        Delta = T_B - Cap_R[index]
        T_Deltas.append(Cap_R[index])
        calc_weighted_budget(Delta, index + 1, T_Deltas, Cap_R, K_R)
    else:
        T_Deltas.append(T_B)
        a = np.asarray(T_Deltas)
        b = np.asarray(K_R)
        b = b[:len(T_Deltas)]

        T_wb = np.dot(a, b) / np.sum(a)
        print()

    return T_wb


T_Budget = 100

Cap_Resource = [40, 30, 50]

K_Resource = [20, 25, 30]

Weighted_Budget = calc_weighted_budget(T_Budget, 0, [], Cap_Resource, K_Resource)
