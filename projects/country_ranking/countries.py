import itertools
countries_and_aliases = {
'Abkhazia': ['Abkhazia '],
'Afghanistan': ['Afghanistan'],
'Albania':['Albania'],
'Algeria':['Algeria'],
'Andorra':['Andorra'],
'Angola':['Angola'],
'Antigua and Barbuda':['Antigua and Barbuda'],
'Argentina':['Argentina'],
'Armenia':['Armenia'],
'Australia':['Australia'],
'Austria':['Austria'],
'Azerbaijan':['Azerbaijan'],
'Bahamas':['Bahamas','Bahamas, The'],
'Bahrain':['Bahrain'],
'Bangladesh':['Bangladesh'],
'Barbados':['Barbados'],
'Belarus':['Belarus'],
'Belgium':['Belgium'],
'Belize':['Belize'],
'Benin':['Benin'],
'Bhutan':['Bhutan'],
'Bolivia':['Bolivia', 'Bolivia (Plurinational State of)'],
'Bosnia and Herzegovina':['Bosnia and Herzegovina','Bosnia And Herzegovina', "Bosnia-Herzegovina"],
'Botswana': ['Botswana'],
'Brazil': ['Brazil'],
'Brunei': ['Brunei','Brunei Darussalam'],
'Bulgaria': ['Bulgaria'],
'Burkina Faso': ['Burkina Faso'],
'Burundi': ['Burundi'],
'Cambodia': ['Cambodia'],
'Cameroon': ['Cameroon'],
'Canada': ['Canada'],
'Cape Verde': ['Cape Verde','Cabo Verde'],
'Central African Republic': ['Central African Republic'],
'Chad': ['Chad'],
'Chile': ['Chile'],
'China': ['China'],
'Colombia': ['Colombia'],
'Comoros': ['Comoros'],
'Democratic Republic of the Congo': ['The Democratic Republic Of The Congo','Congo, Dem. Rep.','Congo, Democratic Republic of (Kinshasa)','Democratic Republic of the Congo','Congo (Democratic Republic of the)'],
'Republic of the Congo': ['Congo, Rep.','Congo, Republic of (Brazzaville)', 'Congo'],
'Costa Rica': ['Costa Rica'],
'Crimea': ['Crimea '],
'Croatia': ['Croatia'],
'Cuba': ['Cuba'],
'Cyprus': ['Cyprus'],
'Czech Republic': ['Czech Republic', 'Czechia'],
"Ivory Coast": ["Côte d'Ivoire","Cote d'Ivoire",'Ivory Coast'],
'Denmark': ['Denmark'],
'Djibouti': ['Djibouti'],
'Dominica': ['Dominica'],
'Dominican Republic': ['Dominican Republic'],
'Ecuador': ['Ecuador'],
'Egypt': ['Egypt','Egypt, Arab Rep.'],
'El Salvador': ['El Salvador'],
'Equatorial Guinea': ['Equatorial Guinea'],
'Eritrea': ['Eritrea'],
'Estonia': ['Estonia'],
'Eswatini': ['Eswatini', 'Eswatini (Kingdom of)'],
'Ethiopia': ['Ethiopia'],
'Faroe Islands':['Faroe Islands'],
'Fiji': ['Fiji'],
'Finland': ['Finland'],
'France': ['France'],
'Gabon': ['Gabon'],
'Gambia, The': ['Gambia, The','Gambia'],
'Gaza Strip': ['Gaza Strip '],
'Georgia': ['Georgia'],
'Germany': ['Germany'],
'Ghana': ['Ghana'],
'Greece': ['Greece'],
'Grenada': ['Grenada'],
'Guatemala': ['Guatemala'],
'Guinea': ['Guinea'],
'Guinea-Bissau': ['Guinea-Bissau','Guinea Bissau'],
'Guyana': ['Guyana'],
'Haiti': ['Haiti'],
'Honduras': ['Honduras'],
'Hong Kong': ['Hong Kong SAR', 'Hong Kong SAR, China','Hong Kong ','Hong Kong, China (SAR)','China, Hong Kong Special Administrative Region'],
'Hungary': ['Hungary'],
'Iceland': ['Iceland'],
'India': ['India'],
'Indian Kashmir': ['Indian Kashmir'],
'Indonesia': ['Indonesia'],
'Iran': ['Iran', 'Iran (Islamic Republic of)','Iran, Islamic Rep.','Islamic Republic of Iran'],
'Iraq': ['Iraq','Iraq','Iraq (Central Iraq)','Iraq (Kurdistan Region)'],
'Ireland': ['Ireland'],
'Israel': ['Israel'],
'Italy': ['Italy'],
'Jamaica': ['Jamaica'],
'Japan': ['Japan'],
'Jordan': ['Jordan'],
'Kazakhstan': ['Kazakhstan'],
'Kenya': ['Kenya'],
'Kiribati': ['Kiribati'],
'Kosovo': ['Kosovo'],
'Kuwait': ['Kuwait'],
'Kyrgyzstan': ['Kyrgyzstan','Kyrgyz Republic'],
'Laos': ['Laos', "Lao People's Democratic Republic",'Lao PDR'],
'Latvia': ['Latvia'],
'Lebanon': ['Lebanon'],
'Lesotho': ['Lesotho'],
'Liberia': ['Liberia'],
'Libya': ['Libya'],
'Liechtenstein': ['Liechtenstein'],
'Lithuania': ['Lithuania'],
'Luxembourg': ['Luxembourg'],
'Macedonia': ['Macedonia', 'The former Yugoslav Republic of Macedonia','North Macedonia'],
'Madagascar': ['Madagascar'],
'Malawi': ['Malawi'],
'Malaysia': ['Malaysia'],
'Maldives': ['Maldives'],
'Mali': ['Mali'],
'Malta': ['Malta'],
'Marshall Islands': ['Marshall Islands'],
'Mauritania': ['Mauritania'],
'Mauritius': ['Mauritius'],
'Mayotte':['Mayotte'],
'Mexico': ['Mexico'],
'Micronesia': ['Micronesia','Federated States of Micronesia', 'Micronesia (Federated States of)','Micronesia, Fed. Sts.'],
'Moldova': ['Moldova', 'Moldova (Republic of)','Republic of Moldova'],
'Monaco': ['Monaco'],
'Mongolia': ['Mongolia'],
'Montenegro': ['Montenegro'],
'Morocco': ['Morocco'],
'Mozambique': ['Mozambique'],
'Myanmar': ['Myanmar'],
'Nagorno-Karabakh': ['Nagorno-Karabakh '],
'Namibia': ['Namibia'],
'Nauru': ['Nauru'],
'Nepal': ['Nepal'],
'Netherlands': ['Netherlands'],
'New Zealand': ['New Zealand'],
'Nicaragua': ['Nicaragua'],
'Niger': ['Niger'],
'Nigeria': ['Nigeria'],
'North Korea': ['North Korea','Korea, Dem. People’s Rep.','Korea, North',"Korea (Democratic People's Rep. of)","Democratic People's Republic of Korea"],
'Northern Cyprus': ['Northern Cyprus','Cyprus North'],
'Norway': ['Norway'],
'Oman': ['Oman'],
'Pakistan': ['Pakistan'],
'Pakistani Kashmir': ['Pakistani Kashmir'],
'Palau': ['Palau'],
'Panama': ['Panama'],
'Papua New Guinea': ['Papua New Guinea'],
'Paraguay': ['Paraguay'],
'Peru': ['Peru'],
'Philippines': ['Philippines','Philippines'],
'Poland': ['Poland'],
'Portugal': ['Portugal'],
'Reunion':['Réunion'],
'Qatar': ['Qatar'],
'Romania': ['Romania'],
'Russia': ['Russia', 'Russian Federation'],
'Rwanda': ['Rwanda'],
'Samoa': ['Samoa'],
'Saint Helena':['Saint Helena'],
'San Marino': ['San Marino'],
'Saudi Arabia': ['Saudi Arabia'],
'Senegal': ['Senegal'],
'Serbia': ['Serbia'],
'Seychelles': ['Seychelles'],
'Sierra Leone': ['Sierra Leone'],
'Singapore': ['Singapore'],
'Slovakia': ['Slovakia','Slovak Republic'],
'Slovenia': ['Slovenia'],
'Solomon Islands': ['Solomon Islands'],
'Somalia': ['Somalia'],
'Somaliland': ['Somaliland '],
'South Africa': ['South Africa'],
'South Korea': ['Korea, Republic of','South Korea[4]','Korea','Korea, Rep.','South Korea','Korea, South', 'Korea (Republic of)','Republic of Korea'],
'South Ossetia': ['South Ossetia '],
'South Sudan': ['South Sudan'],
'Spain': ['Spain'],
'Sri Lanka': ['Sri Lanka','Sri Lanka'],
'St. Kitts and Nevis': ['St. Kitts and Nevis', 'Saint Kitts and Nevis','St Kitts and Nevis'],
'St. Lucia': ['St. Lucia','Saint Lucia','St Lucia'],
'St. Vincent and Grenadines': ['St Vincent and the Grenadines','St. Vincent and the Grenadines','St. Vincent and Grenadines','Saint Vincent and the Grenadines'],
'Sudan': ['Sudan'],
'Suriname': ['Suriname'],
'Swaziland': ['Swaziland'],
'Sweden': ['Sweden'],
'Switzerland': ['Switzerland'],
'Syria': ['Syria','Syrian Arab Republic'],
'Sao Tome and Principe': ['São Tomé and Príncipe', 'Sao Tome and Principe'],
'Taiwan': ['Taiwan', 'China, Taiwan Province of China'],
'Tajikistan': ['Tajikistan'],
'Tanzania': ['Tanzania', 'Tanzania (United Republic of)','United Republic of Tanzania'],
'Thailand': ['Thailand'],
'Tibet': ['Tibet '],
'Timor-Leste': ['Timor-Leste','East Timor'],
'Togo': ['Togo'],
'Tonga': ['Tonga'],
'Transnistria': ['Transnistria'],
'Trinidad and Tobago': ['Trinidad and Tobago'],
'Tunisia': ['Tunisia'],
'Turkey': ['Turkey'],
'Turkmenistan': ['Turkmenistan'],
'Tuvalu': ['Tuvalu'],
'Uganda': ['Uganda'],
'Ukraine': ['Ukraine','Ukraine Україна (Translation)'],
'United Arab Emirates': ['United Arab Emirates'],
'United Kingdom': ['UK','United Kingdom','United Kingdom (England and Wales)',
'United Kingdom (Northern Ireland)',
'United Kingdom (Scotland)',
'United Kingdom of Great Britain and Northern Ireland'],
'United States': ['US','United States','United States of America'],
'Uruguay': ['Uruguay'],
'Uzbekistan': ['Uzbekistan'],
'Vanuatu': ['Vanuatu'],
'Venezuela': ['Venezuela', 'Venezuela (Bolivarian Republic of)','Venezuela, RB'],
'Vietnam': ['Vietnam', 'Viet Nam'],
'Palestine, State of': ['Palestine','West Bank','State of Palestine','West Bank and Gaza','Palestinian Territory'],
'Western Sahara': ['Western Sahara '],
'Yemen': ['Yemen','Yemen, Rep.'],
'Zambia': ['Zambia'],
'Zimbabwe': ['Zimbabwe'],
'Anguilla':['Anguilla'],
'Aruba':['Aruba'],
'British Virgin Islands':['British Virgin Islands','Virgin Islands'],
'Cayman Islands':['Cayman Islands'],
'Curaçao':['Curaçao','Curacao'],
'Guadeloupe':['Guadeloupe'],
'Martinique':['Martinique'],
'Montserrat':['Montserrat'],
'Puerto Rico':['Puerto Rico'],
'Turks and Caicos Islands':['Turks and Caicos Islands'],
'United States Virgin Islands':['United States Virgin Islands','Virgin Islands (U.S.)'],
'Bermuda':['Bermuda'],
'Greenland':['Greenland'],
'St. Martin (French part)':['St. Martin (French part)'],
'Sint Maarten (Dutch part)':['Sint Maarten (Dutch part)','St Maarten'],
'Saint Pierre and Miquelon':['Saint Pierre and Miquelon'],
'French Guiana':['French Guiana'],
'China, Macao Special Administrative Region':['Macau','Macao SAR, China','China, Macao Special Administrative Region'],
'Channel Islands':['Channel Islands', 'Guernsey', 'Jersey'],
'Isle of Man':['Isle of Man'],
'Gibraltar':['Gibraltar'],
'Holy See':['Holy See'],
'Kosovo':['Kosovo under UNSCR 1244'],
'New Caledonia':['New Caledonia'],
'Guam':['Guam'],
'Canary Islands':['Canary Islands'],
'American Samoa':['American Samoa'],
'Cook Islands':['Cook Islands'],
'French Polynesia':['French Polynesia'],
'Niue':['Niue'],
'Northern Mariana Islands':['Northern Mariana Islands'],
'Bonaire, Saint Eustatius and Saba':['Bonaire, Saint Eustatius and Saba'],
'Netherlands Antilles':['Netherlands Antilles'],

}

all_country_aliases = list(itertools.chain.from_iterable(countries_and_aliases.values()))