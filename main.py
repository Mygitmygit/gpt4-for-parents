# openai install 부터 하기
import openai
import streamlit as st

 




def gen(x):
  gpt_prompt =[{"role": "system","content": "Answer in korean."}]
  gpt_prompt.append({"role":"user","content": x})
  gpt_response = openai.ChatCompletion.create(model="gpt-4",messages=gpt_prompt,temperature=0.5)
  return gpt_response["choices"][0]["message"]["content"]



def process_input(input_text):
    processed_output = gen(input_text)
    return processed_output



# streamlit app
def main():
    st.title("무엇이든 물어보세요")

    user_input = st.text_area("질문을 입력해주세요:",height=150)

    if st.button("질문하기"):
        processed_output = process_input(user_input)
        st.text("답변:")
        st.write(processed_output)

if __name__ == "__main__":
    main()

