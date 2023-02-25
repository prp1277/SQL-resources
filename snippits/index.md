# Helpful snippits and templates for Microsoft Access Queries

## Calculate records greater than `x` years old

```sql
<DateSerial(Year(Now())-[x],Month(Now()),Day(Now()))
```

## Calculate records less than `x` years old
```sql
>=DateSerial(Year(Now())-1,Month(Now()),Day(Now()))
```