from gtts import gTTS
import os

text = "آرٹیفیشل انٹیلیجنس، جسے اردو میں مصنوعی ذہانت کہتے ہیں، موجودہ دور کی ایک اہم اور انقلابی ٹیکنالوجی ہے۔ یہ وہ شعبہ ہے جس میں کمپیوٹرز اور مشینوں کو اس قابل بنایا جاتا ہے کہ وہ انسانی ذہانت کی طرح سوچ سکیں، فیصلے کر سکیں، اور مختلف مسائل کو حل کرنے کی صلاحیت حاصل کریں۔ مصنوعی ذہانت آج کل کے دور میں زندگی کے ہر شعبے میں استعمال ہو رہی ہے اور اس کی اہمیت دن بدن بڑھ رہی ہے۔مصنوعی ذہانت سے مراد وہ نظام یا مشینیں ہیں جو انسانی ذہانت کی نقل کر کے کام کر سکتی ہیں۔ ان مشینوں میں خودکار طریقے سے سیکھنے، سمجھنے، اور مسائل حل کرنے کی صلاحیت پیدا کی جاتی ہے۔ یہ نظام کمپیوٹر سائنس، میتھمیٹکس، اور دیگر جدید علوم کی مدد سے تیار کیے جاتے ہیں۔مصنوعی ذہانت ایک حیرت انگیز ایجاد ہے جو انسانیت کے لیے فائدے مند ثابت ہو رہی ہے۔ لیکن اس کے ساتھ ہمیں اس بات کا بھی خیال رکھنا ہوگا کہ اس ٹیکنالوجی کو مثبت اور اخلاقی مقاصد کے لیے استعمال کیا جائے۔ اگر ہم مصنوعی ذہانت کو صحیح طریقے سے استعمال کریں تو یہ انسانی زندگی کو بہتر بنانے میں بے حد مددگار ثابت ہو سکتی ہے۔"

language = 'ur'

tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)

os.system(f"start {audio_file}")  # Use 'start' for Windows, 'open' for macOS, 'xdg-open' for Linux

print(f"Audio saved as {audio_file}")