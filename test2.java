Calendar sameDate = Calendar.getInstance();

sameDate.set(Calendar.YEAR, 2010);
// Month. 0 is January, 11 is November
sameDate.set(Calendar.MONTH, Calendar.AUGUST);
sameDate.set(Calendar.DAY_OF_MONTH, 23);

// Either 12-hour clock plus AM/PM
sameDate.set(Calendar.HOUR, 10);
sameDate.set(Calendar.AM_PM, Calendar.PM);
// or 24-hour clock
sameDate.set(Calendar.HOUR_OF_DAY, 22);

sameDate.set(Calendar.MINUTE, 36);
sameDate.set(Calendar.SECOND, 22);
sameDate.set(Calendar.MILLISECOND, 123);

System.out.println("Some Date : " + sameDate.getTime());
