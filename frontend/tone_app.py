import requests
import streamlit as st

PREDICTION_API_URL = "http://localhost:8000/api/predict/"


def get_tone_prediction(message):
    """function which make response on internal service and take answer

    Args:
        message (_type_): responsed text

    Returns:
        answer from internal service
    """
    response = requests.post(PREDICTION_API_URL, json={"text": message})
    if response.status_code == 200:
        response_dict = dict(response.json())
        label, score = response_dict.get("label"), str(response_dict.get("score"))
        answer = f"Sentiment: **{label}**  \nScore: **{score}**"

        return answer

    else:
        answer = f"Error during request with status code: {response.status_code}"
        return answer


# Streamlit app


def main():
    st.title("Sentiment predictor chat")
    st.markdown("This app requires running the prediction model inference")

    # Initialize session state variables
    if "message" not in st.session_state:
        st.session_state.message = ""
    if "tone" not in st.session_state:
        st.session_state.tone = None

    st.write("Enter a message to get its tone prediction from the model:")
    message = st.text_area(
        "Your message:", value=st.session_state.message, key="message"
    )

    if st.button("predict tonality"):
        if message:
            st.session_state.tone = get_tone_prediction(message)
            # st.success(f"The predicted result: {tonality}")
        else:
            st.error("Please enter a text to get a prediction")
    if st.session_state.tone:
        st.success(f"The predicted tone is: {st.session_state.tone}")


if __name__ == "__main__":
    main()
