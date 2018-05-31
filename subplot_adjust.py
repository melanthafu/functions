# distribution plots for loan_amount, down_payment_amount, user_dob_year and fico_score
fig = plt.figure(figsize=(16, 10))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=0.5)

ct = 1
for i in de_corr:
    temp = df[[i, 0]].groupby(i).mean().reset_index(drop = False)
    plt.subplot(9,4,ct)
    sns.barplot(x = 0, y = i, data = temp)
    plt.xlabel(str(i))
    plt.xticks([])
    ct += 1
plt.show()