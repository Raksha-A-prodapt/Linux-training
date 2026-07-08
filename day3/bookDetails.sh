#!/bin/bash

file="book.txt"

echo "=========================="
echo "   Display Book Details   "

display_records() {
    echo "========= Book Records =========="
    cat "$file"
}

display_details() {
    echo "Enter the name of the Book"
    read a

    if grep -qi "$a" "$file"
    then
        echo "Book found"
        grep -i "$a" "$file"
    else
        echo "Book not found"
    fi
}

book_out_stock() {
    count=$(grep -c "OutOfStock" "$file")
    echo "No. of books Out Of Stock: $count"
}

update_stock_status() {
    echo "Enter BookId:"
    read id

    if grep -q "^$id," "$file"
    then
        sed -i "/^$id,/ s/Available/OutOfStock/" "$file"
        echo "Stock status updated."
    else
        echo "Book ID not found."
    fi
}

tot_ivt_value() {
    total=$(awk -F',' '{sum+=$5} END{print sum}' "$file")
    echo "Total Inventory Value: $total"
}

disp_cat() {
    echo "Enter Category:"
    read cat

    awk -F',' -v c="$cat" 'tolower($3)==tolower(c)' "$file"
}

costliest() {
    echo "Costliest Book"

    awk -F',' '
    BEGIN {
        max=0
    }
    {
        if ($5 > max) {
            max=$5
            book=$2
        }
    }
    END {
        print "Costliest Book is: " book
        print "Cost of the Book: " max
    }
    ' "$file"
}

while true
do
    echo "======================================"
    echo "1.Display Books"
    echo "2.Display Details"
    echo "3.Display Books Out Of Stock"
    echo "4.Update Stock"
    echo "5.Total Inventory Value"
    echo "6.Category Books"
    echo "7.High Cost"
    echo "8.Exit"

    echo "Enter choice:"
    read ch

    case $ch in
        1)
            display_records
            ;;
        2)
            display_details
            ;;
        3)
            book_out_stock
            ;;
        4)
            book_out_stock            
            ;;
        5)
            tot_ivt_value
            ;;
        6)
            disp_cat
            ;;
        7)
            costliest
            ;;
        8)
            break
            ;;
        *)
            echo "Invalid Choice"
            ;;
    esac

done
