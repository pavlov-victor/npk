def save_results(result, name, tracks=[]):
    with open('/results/' + name + '_result.txt', 'w+') as f:
        f.write(f'{name}: result - {result}\n')
        for track in tracks:
            f.write(f'{name}: {track}')
