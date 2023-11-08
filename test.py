from evaluator import Evaluator
import spec_utils

if __name__ == "__main__":
    column_groups = [
        spec_utils.get_wavelengths()
    ]

    c = Evaluator(prefix="t2", folds=10, algorithms=["ann_savi_only","ann_savi"], column_groups=column_groups)
    c.process()