import streamlit as st 

from web_functions import predict

def app(df, x, y):
    
    st.title("Halaman Prediksi Batu Ginjal")
    st.text("1 = Ya \n0 = Tidak")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input('Tekanan Darah', value=0)
        sg = st.text_input('Kepadatan Urin', value=0)
        al = st.text_input('Albumin Urin', value=0)
        su = st.text_input('Sedimen Urin', value=0)
        rbc = st.text_input('Sel Darah Merah dalam Urin', value=0)
        pc = st.text_input('Sel Darah Putih dalam Urin', value=0)
        pcc = st.text_input('Tingkat Keparahan Leukosit dalam Urin', value=0)
        ba = st.text_input('Bakteri dalam Urin', value=0)

    with col2:
        bgr = st.text_input('Kadar Gula Darah', value=0)
        bu = st.text_input('Kadar Urea Darah', value=0)
        sc = st.text_input('Kadar Kreatinin dalam Darah', value=0)
        sod = st.text_input('Kadar Natrium dalam Darah', value=0)
        pot = st.text_input('Kadar Kalium dalam Darah', value=0)
        hemo = st.text_input('Kadar Hemoglobin dalam Darah', value=0)
        pcv = st.text_input('Hematokrit (Persentase Sel Darah Merah)', value=0)
        wc = st.text_input('Sel Darah Putih dalam Darah', value=0)

    with col3:
        rc = st.text_input('Sel Darah Merah dalam Darah', value=0)
        htn = st.text_input('Hipertensi (Tekanan Darah Tinggi)', value=0)
        dm = st.text_input('Diabetes Melitus', value=0)
        cad = st.text_input('Penyakit Jantung Koroner', value=0)
        appet = st.text_input('Nafsu Makan', value=0)
        pe = st.text_input('Pembengkakan (Edema)', value=0)
        ane = st.text_input('Anemia (Kekurangan Sel Darah Merah)', value=0)

    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]

    # tombol prediksi 
    if st.button('Prediksi'):
        # proses prediksi
        prediction, score = predict(x,y, features)
        score = score
        st.info("Prediksi Sukses..")
    
        if(prediction==1):
            st.warning("Orang tersebut rentan terkena penyakit ginjal")
        else:
            st.success("Orang tersebut relatif aman dari penyakit ginjal")
            
        #st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")