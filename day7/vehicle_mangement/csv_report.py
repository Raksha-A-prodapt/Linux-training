import csv
def  export_vehicle_data(filename,vehicles):
    with open(filename,mode="w", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["Brand","Model","Year","Owner","battery_Capacity"])
        for v in vehicles:
            owner=v.get_owner()#.replace('owner: ',"")
            if owner is None:
                owner="NO OWNER ASSIGNED"
            battery_Capacity=getattr(v,"battery_capacity",'N/A')
            writer.writerow([v.brand,v.model,v.year,owner,battery_Capacity])

    return f"Vehicle data exported to {filename}  scuccessfully!"