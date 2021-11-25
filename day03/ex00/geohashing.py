import sys
import antigravity


if __name__ == "__main__":
    if sys.argv.count() == 4:
        date = bytes(f'{sys.argv[3]}', encoding='utf-8')
        antigravity.geohash(float(sys.argv[1]),float(sys.argv[2]), date)