from data import DataLoader

if __name__ == '__main__':
    songs = DataLoader.load()
    print(f'There are {len(songs)} in total')
