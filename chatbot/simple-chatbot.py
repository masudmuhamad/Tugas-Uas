import string

#gunakan nama chatbot mu sesuai yang diinginkan
chatbot_name = "Masta" + "Bot"

#gunakan sentinel looping : yang berguna untuk menjalankan perintah chatbot sampai user bilang berhenti
while True :

	#memasukan inputan pertama
	user_message = input("anda: ").lower().strip(string.punctuation+string.whitespace)

	#respon dari chatbot
	print(chatbot_name + ":",)

	#mengakhiri percakapan
	if user_message == "quit" or user_message == "selesai":
		print("sampai jumpa lagi")
		break

	if user_message == "halo":
		print(chatbot_name + ": halo juga", end=' ')
	elif user_message == "apa kabar":
		print(chatbot_name + ": kabarku baik bagaimana denganmu?", end=' ')
	elif user_message == "siapa namamu" or "siapa nama kamu?":
		print(chatbot_name + ": namaku MastaBot", end=' ')
	elif user_message == "apa yang bisa kamu lakukan?":
		print(chatbot_name + ": menjawab pertanyaan sederhana darimu", end=' ')
	else:
		print(chatbot_name + ": loh, kamu ngomong apa aku gak ngerti nih!")
		print()




