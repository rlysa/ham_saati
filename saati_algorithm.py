from types import SimpleNamespace

def oksv_and_novp_no_print(matrix):
    n = len(matrix)
    geom_means = []
    for row in matrix:
        prod = 1.0
        for x in row:
            prod *= x
        geom_means.append(prod ** (1.0 / n))
    total = sum(geom_means)
    return [gm / total for gm in geom_means]


def run_saati(criteria_names, alt_names, crit_matrix, obj_matrices):
    criteria_weights = oksv_and_novp_no_print(crit_matrix)

    objects_weights_per_criterion = []
    for mat in obj_matrices:
        w = oksv_and_novp_no_print(mat)
        objects_weights_per_criterion.append(w)

    num_alts = len(alt_names)
    final_scores = [0.0] * num_alts
    for j in range(num_alts):
        for i, crit_w in enumerate(criteria_weights):
            final_scores[j] += crit_w * objects_weights_per_criterion[i][j]

    ranked = sorted(
        zip(alt_names, final_scores),
        key=lambda x: x[1],
        reverse=True
    )
    ranking = [name for name, _ in ranked]

    return SimpleNamespace(
        normalized_criteria_matrix=crit_matrix,
        criteria_weights=criteria_weights,
        objects_weights_per_criterion=objects_weights_per_criterion,
        final_scores=final_scores,
        ranking=ranking
    )
