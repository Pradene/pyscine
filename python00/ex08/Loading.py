import sys


def ft_tqdm(lst: range):
    length = 48
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        fraction = i / total
        filled_length = int(length * fraction)
        bar = '█' * filled_length + ' ' * (length - filled_length)
        percent = fraction * 100
        sys.stdout.write(
            f"\r{round(percent):3}%|{bar}| "
            f"{i}/{total}"
        )
        sys.stdout.flush()
        yield item
    sys.stdout.write('\n')
    sys.stdout.flush()
    return
