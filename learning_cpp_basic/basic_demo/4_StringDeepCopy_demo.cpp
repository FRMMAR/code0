# include <iostream>
# include <string>

class String
{
	private:
	char * str;
	public:
	String ():str(new char[1]) { str[0] = 0;}
	const char * c_str() { return str; };
	String & operator = (const char * s)
	{
		if( this == & s)
			return * this;
		delete [] str;
		str = new char[strlen(s)+1];
		strcpy( str, s);
		return * this;
	};
	~String( ) { delete [] str; }
};
