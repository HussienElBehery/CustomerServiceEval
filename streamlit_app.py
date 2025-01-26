import streamlit as st
import numpy as np

# Mock prediction functions - replace with your actual model
def predict_sentiment(text):
    # Replace with your sentiment model prediction
    return np.random.choice(['Positive', 'Neutral', 'Negative']), np.random.rand()

def predict_politeness(text):
    # Replace with your politeness model prediction
    return np.random.rand()

def main():
    st.set_page_config(page_title="Chat Analysis Dashboard", layout="wide")
    st.title("💬 Chat Conversation Analyzer")
    
    # Input section
    with st.container():
        st.subheader("📥 Input Chat Conversation")
        chat_input = st.text_area("Paste customer-agent chat here:", 
                                height=200,
                                placeholder="Customer: Hello, I'm having issues with my order...\nAgent: Hi! Let me help you with that...")
    
    if st.button("Analyze Conversation", type="primary"):
        if chat_input:
            with st.spinner("Analyzing conversation..."):
                # Get predictions (replace with actual model calls)
                sentiment, confidence = predict_sentiment(chat_input)
                politeness_score = predict_politeness(chat_input)
                
                # Create layout columns
                col1, col2 = st.columns(2)
                
                # Sentiment Analysis Card
                with col1:
                    st.subheader("😊 Sentiment Analysis")
                    
                    # Sentiment visualization
                    sentiment_color = {
                        'Positive': '#4CAF50',
                        'Neutral': '#FFC107',
                        'Negative': '#F44336'
                    }.get(sentiment, '#000000')
                    
                    st.markdown(f"""
                    <div style="
                        padding: 20px;
                        border-radius: 10px;
                        background-color: {sentiment_color}10;
                        border-left: 5px solid {sentiment_color};
                        margin: 10px 0;">
                        <h3 style="color: {sentiment_color}; margin:0">{sentiment} Sentiment</h3>
                        <p style="margin: 10px 0">Confidence: {confidence:.0%}</p>
                        <div style="
                            height: 10px;
                            background-color: #eee;
                            border-radius: 5px;">
                            <div style="
                                width: {confidence*100}%;
                                height: 100%;
                                background-color: {sentiment_color};
                                border-radius: 5px;">
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Politeness Analysis Card
                with col2:
                    st.subheader("🤝 Politeness Metric")
                    
                    # Determine politeness level
                    politeness_level = "High" if politeness_score >= 0.7 else \
                                    "Medium" if politeness_score >= 0.4 else "Low"
                    
                    politeness_color = {
                        'High': '#4CAF50',
                        'Medium': '#FFC107',
                        'Low': '#F44336'
                    }.get(politeness_level, '#000000')
                    
                    st.markdown(f"""
                    <div style="
                        padding: 20px;
                        border-radius: 10px;
                        background-color: {politeness_color}10;
                        border-left: 5px solid {politeness_color};
                        margin: 10px 0;">
                        <h3 style="color: {politeness_color}; margin:0">{politeness_level} Politeness</h3>
                        <p style="margin: 10px 0">Score: {politeness_score:.2f}/1.00</p>
                        <div style="
                            height: 10px;
                            background-color: #eee;
                            border-radius: 5px;">
                            <div style="
                                width: {politeness_score*100}%;
                                height: 100%;
                                background-color: {politeness_color};
                                border-radius: 5px;">
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Add some space
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Conversation breakdown section
                st.subheader("🧐 Conversation Breakdown")
                col3, col4 = st.columns(2)
                
                with col3:
                    st.markdown("**Key Sentiment Indicators**")
                    st.write("- Positive language: 12 instances")
                    st.write("- Neutral statements: 8 instances")
                    st.write("- Negative phrases: 3 instances")
                
                with col4:
                    st.markdown("**Politeness Factors**")
                    st.write("- Greetings used: 2 times")
                    st.write("- Polite modifiers: 5 instances")
                    st.write("- Empathetic phrases: 4 instances")
                    
        else:
            st.warning("⚠️ Please enter a conversation to analyze")

if __name__ == "__main__":
    main()