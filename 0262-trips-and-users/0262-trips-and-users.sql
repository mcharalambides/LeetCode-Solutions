select request_at as Day, ROUND(IFNULL(cancellations/count(*),0.00),2) as `Cancellation Rate` from Trips
left join 
    (select request_at as Day,count(*) as cancellations
    from Trips 
    inner join Users urs1 on Trips.client_id = urs1.users_id and urs1.banned = 'No'
    inner join Users urs2 on Trips.driver_id  = urs2.users_id and urs2.banned = 'No'
    where status like 'cancelled%' and (Trips.request_at between "2013-10-01" and "2013-10-03")
    Group By request_at) temp on Trips.request_at = temp.Day
inner join Users urs1 on Trips.client_id = urs1.users_id and urs1.banned = 'No'
inner join Users urs2 on Trips.driver_id  = urs2.users_id and urs2.banned = 'No'
where (Trips.request_at between "2013-10-01" and "2013-10-03")
Group by Trips.request_at