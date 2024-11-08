package models

type Profile struct {
	ID           int    `json:"id" gorm:"primaryKey, autoIncrement"`
	Name         string `json:"name"`
	URL 		 string `json:"url"`
	Nickname     string `json:"nickname"`
	Public_Info  string `json:"public_info"`
	Messaging    string `json:"messaging"`
	Biography    string `json:"biography"`
	Organization string `json:"organization"`
	Country      string `json:"country"`
	Social_Media string `json:"social_media"`
	Email        string `json:"email"`
}
