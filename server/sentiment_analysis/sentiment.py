import fasttext



def review(text):
    label1 = 0
    model = fasttext.load_model('model_reviews.bin')
    label2 = 0
    for data in text:
        a = model.predict(data)
        if "label" in a[0][0]:
            label1 = label1+a[1][0]
        elif "label2" in a[0][0]:
            label2 = label2 + a[1][0]
        
    if label2 > label1:
        return 1
    else:
        return -1
