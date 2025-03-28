import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Basic Data Cleaner & Converter")

file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if file:
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.write("### Original Data")
    st.dataframe(df)

    if st.button("Remove Duplicates"):
        df = df.drop_duplicates()
        st.write("### Cleaned Data")
        st.dataframe(df)

    st.write("### Download File")

    convert_to = st.radio("Convert File To:", ["CSV", "Excel"])

    if st.button("Download Converted File"):
        output = BytesIO()
        if convert_to == "CSV":
            df.to_csv(output, index=False)
            file_name = "converted_file.csv"
            mime_type = "text/csv"
        else:
            df.to_excel(output, index=False, engine='openpyxl')
            file_name = "converted_file.xlsx"
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        output.seek(0)
        st.download_button("⬇️ Download File", data=output, file_name=file_name, mime=mime_type)

st.success("🎉 Done! Upload, Clean & Convert your files easily.")  
