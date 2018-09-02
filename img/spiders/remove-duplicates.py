import os
import reusables


def remove_duplicates(directory):
    sizes = {}

    for file in reusables.find_files(directory):
        file_size = os.path.getsize(file)
        if file_size not in sizes:
            sizes[file_size] = [file]
        else:
            sizes[file_size].append(file)

    size_matches = [v for v in sizes.values() if len(v) > 1]

    hashes = {}
    for possible_duplicates in size_matches:
        for dd in possible_duplicates:
            file_hash = reusables.file_hash(dd)
            if file_hash not in hashes:
                hashes[file_hash] = [dd]
            else:
                hashes[file_hash].append(dd)

    return [v for v in hashes.values() if len(v) > 1]


if __name__ == '__main__':
    path = "images"
    results = remove_duplicates(path)
    print(len(results), results)
    for file in results:
        for i in range(len(file)):
            if i is 0:
                continue
            else:
                os.remove(file.pop())



