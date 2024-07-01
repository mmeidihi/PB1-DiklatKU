import streamlit as st

def app():
    st.title('About the Mushroom Datasets')

    st.write("""
    Dataset "Mushroom Classification" dari UCI Machine Learning Repository yang tersedia di Kaggle memiliki struktur berikut:

### Isi Dataset:
Dataset ini terdiri dari 23 kolom yang mencakup berbagai fitur atau karakteristik morfologi jamur, serta satu kolom target yang menunjukkan keberacayaan jamur (beracun atau aman dikonsumsi). Berikut adalah daftar kolom yang ada dalam dataset:

1. *class*: Variabel target yang menunjukkan apakah jamur beracun ('p': poisonous) atau aman dikonsumsi ('e': edible).
   
2. *cap-shape*: Bentuk tutup jamur (b: bell, c: conical, x: convex, f: flat, k: knobbed, s: sunken).
   
3. *cap-surface*: Permukaan tutup jamur (f: fibrous, g: grooves, y: scaly, s: smooth).
   
4. *cap-color*: Warna tutup jamur (n: brown, b: buff, c: cinnamon, g: gray, r: green, p: pink, u: purple, e: red, w: white, y: yellow).
   
5. *bruises*: Memar pada jamur (t: bruises, f: no bruises).
   
6. *odor*: Bau jamur (a: almond, l: anise, c: creosote, y: fishy, f: foul, m: musty, n: none, p: pungent, s: spicy).
   
7. *gill-attachment*: Lampiran gill jamur (a: attached, d: descending, f: free, n: notched).
   
8. *gill-spacing*: Jarak gill jamur (c: close, w: crowded, d: distant).
   
9. *gill-size*: Ukuran gill jamur (b: broad, n: narrow).
   
10. *gill-color*: Warna gill jamur (k: black, n: brown, b: buff, h: chocolate, g: gray, r: green, o: orange, p: pink, u: purple, e: red, w: white, y: yellow).
   
11. *stalk-shape*: Bentuk stalk jamur (e: enlarging, t: tapering).
   
12. *stalk-root*: Akar stalk jamur (b: bulbous, c: club, u: cup, e: equal, z: rhizomorphs, r: rooted, ?: missing).
   
13. *stalk-surface-above-ring*: Permukaan stalk di atas cincin (f: fibrous, y: scaly, k: silky, s: smooth).
   
14. *stalk-surface-below-ring*: Permukaan stalk di bawah cincin (f: fibrous, y: scaly, k: silky, s: smooth).
   
15. *stalk-color-above-ring*: Warna stalk di atas cincin (n: brown, b: buff, c: cinnamon, g: gray, o: orange, p: pink, e: red, w: white, y: yellow).
   
16. *stalk-color-below-ring*: Warna stalk di bawah cincin (n: brown, b: buff, c: cinnamon, g: gray, o: orange, p: pink, e: red, w: white, y: yellow).
   
17. *veil-type*: Jenis veil jamur (p: partial, u: universal).
   
18. *veil-color*: Warna veil jamur (n: brown, o: orange, w: white, y: yellow).
   
19. *ring-number*: Jumlah cincin pada jamur (n: none, o: one, t: two).
   
20. *ring-type*: Tipe cincin pada jamur (c: cobwebby, e: evanescent, f: flaring, l: large, n: none, p: pendant, s: sheathing, z: zone).
   
21. *spore-print-color*: Warna spore print jamur (k: black, n: brown, b: buff, h: chocolate, r: green, o: orange, u: purple, w: white, y: yellow).
   
22. *population*: Populasi jamur (a: abundant, c: clustered, n: numerous, s: scattered, v: several, y: solitary).
   
23. *habitat*: Habitat jamur (g: grasses, l: leaves, m: meadows, p: paths, u: urban, w: waste, d: woods).

Setiap entri dalam dataset mewakili satu jamur dengan berbagai fitur morfologi yang dapat digunakan untuk membangun model klasifikasi yang dapat memprediksi keberacayaan jamur berdasarkan karakteristiknya.

    """) 
app() 