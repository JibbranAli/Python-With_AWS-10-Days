import backup
import restore
import list_backup
import delete_backup_folder
import delete_3_backup

while True:
    print("\n===========================")
    print("AWS CLOUD BACKUP SYSTEM ")
    print("\n===========================")
    print("1. Backup Files ")
    print("2. Restore Files ")
    print("3. List Backup ")
    print("4. Delete Backup  ")
    print("5. Delete Last 3 Backup ")
    print("6. EXIT")

    choice = input ("Enter the choice : ")

    if choice == "1":
        backup.backup_file()
    elif choice == "3":
        list_backup.list_backup()
    elif choice == "2":
        restore.restore()
    elif choice == "4":
        delete_backup_folder.delete_backup_folder()
    elif choice == "5":
        delete_3_backup.delete_3_backup()
    elif choice == "6":
        break
    else:
        print("\nEnter Valid Option from 1 to 6" )
        
        