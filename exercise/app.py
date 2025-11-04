from src.dosya_islemleri import read_csv, write_json, write_text
from src.processing import stats, build_report, clean_data
from src.dekorator import required_column

def main():
    read_doc = "/Users/mevanuryazicioglu/Downloads/betik_diller-main/exercise/data/people.csv"
    write_json_doc = "/Users/mevanuryazicioglu/Downloads/betik_diller-main/exercise/data/people_clean.json"
    write_stats_doc = "/Users/mevanuryazicioglu/Downloads/betik_diller-main/exercise/data/stats.json"
    write_txt = "/Users/mevanuryazicioglu/Downloads/betik_diller-main/exercise/data/stats_txt.txt"

    # 1. Oku
    rows = read_csv(read_doc)

    # 2. Şema kontrolü yap (dekoratörü burada çağırıyoruz)
    required_check = required_column({"name", "age", "city"})(lambda r: r)
    rows = required_check(rows)

    # 3. Temizle
    cleaned_rows = clean_data(rows)

    # 4. İstatistik üret
    st = stats(cleaned_rows)

    # 5. Çıktı yaz
    write_json(write_json_doc, cleaned_rows)
    write_json(write_stats_doc, st)
    write_text(write_txt, build_report(st))

    print("İşlem tamamlandı ✅")

if __name__ == "__main__":
    main()
