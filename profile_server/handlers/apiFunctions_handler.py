from flask import Flask, request
from models.Log import Log
from models.Profile import Profile
from database.connection import Connection
from database.queries import *
from communication.communication import sendLog
from security.verificaction import *
import datetime

app = Flask(__name__)
database = Connection()

async def AddProfile_handler():
    try:

        data = request.get_json()

        required_fields = ['name', 'url', 'nickname', 'public_info', 'messaging', 'biography', 'organization', 'country', 'social_media', 'email']
        for field in required_fields:
            if field not in data:
                log = Log(
                    app_name = "PROFILE-API",
                    log_type = "ERROR",
                    module = "ADD-PROFILE",
                    log_date_time = datetime.datetime.now().isoformat(),
                    summary = "Error in information",
                    description = f"Missing field {field}")
                await sendLog(log)
                return 'Error: Missing field ' + field, 400

            if not isinstance(data[field], str):
                log = Log(
                    app_name = "PROFILE-API",
                    log_type = "ERROR",
                    module = "ADD-PROFILE",
                    log_date_time = datetime.datetime.now().isoformat(),
                    summary = "Error in information",
                    description = f"Field is not a String: {field}")
                await sendLog(log)
                return 'Error: Invalid data type for field ' + field + '. Expected string.', 400

        if not isValidToken(request, data['email']):
            log = Log(
            app_name = "PROFILE-API",
            log_type = "ERROR",
            module = "ADD-PROFILE",
            log_date_time = datetime.datetime.now().isoformat(),
            summary = "Failed to registrer profile",
            description = "Invalid token provided")
            await sendLog(log)
            return 'Error: Invalid token provided', 404
        
        if await isEmailTaken(data['email']):
            log = Log(
            app_name = "PROFILE-API",
            log_type = "ERROR",
            module = "ADD-PROFILE",
            log_date_time = datetime.datetime.now().isoformat(),
            summary = "Failed to register profile",
            description = "Email is already taken")
            await sendLog(log)
            return 'Error: Email is already taken', 400
        
        profile = Profile(
            name=data['name'],
            url=data['url'],
            nickname=data['nickname'],
            public_info=data['public_info'],
            messaging=data['messaging'],
            biography=data['biography'],
            organization=data['organization'],
            country=data['country'],
            social_media=data['social_media'],
            email=data['email']
        )

        database.add(profile)
        database.commit()
        database.close()

        log = Log(
            app_name = "PROFILE-API",
            log_type = "INFO",
            module = "ADD-PROFILE",
            log_date_time = datetime.datetime.now().isoformat(),
            summary = "Profile added successfully",
            description = "A profile has been added successfully" 
        )
        await sendLog(log)
        return 'message: Profile created successfully', 200

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        log = Log(
            app_name = "PROFILE-API",
            log_type = "ERROR",
            module = "ADD-PROFILE",
            log_date_time = datetime.datetime.now().isoformat(),
            summary = "Unexpected error",
            description = error_message
        )
        await sendLog(log)
        return 'error: ' + error_message, 400

async def UpdateProfile_handler():
    try:
        data = request.get_json()

        required_fields = ['name', 'url', 'nickname', 'public_info', 'messaging', 'biography', 'organization', 'country', 'social_media', 'email']
        
        for field in required_fields:
            if field in data and not isinstance(data[field], str):
                print("info: " + data[field])
                log = Log(
                    app_name="PROFILE-API",
                    log_type="ERROR",
                    module="UPDATE-PROFILE",
                    log_date_time=datetime.datetime.now().isoformat(),
                    summary="Error in information",
                    description=f"Field is not a String: {field}")
                await sendLog(log)
                return f'Error: Invalid data type for field {field}. Expected string.', 400

        if not isValidToken(request, data.get('email')):
            log = Log(
                app_name="PROFILE-API",
                log_type="ERROR",
                module="UPDATE-PROFILE",
                log_date_time=datetime.datetime.now().isoformat(),
                summary="Failed to update profile",
                description="Invalid token provided")
            await sendLog(log)
            return 'Error: Invalid token provided', 404

        profile = database.query(Profile).filter_by(email=data['email']).first()

        if not profile:
            return 'Error: Profile not found', 404

        for field in required_fields:
            if field in data and data[field]:
                setattr(profile, field, data[field])

        database.commit()

        log = Log(
            app_name="PROFILE-API",
            log_type="INFO",
            module="UPDATE-PROFILE",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Profile updated successfully",
            description="A profile has been updated successfully"
        )
        await sendLog(log)
        return 'message: Profile updated successfully', 200

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        log = Log(
            app_name="PROFILE-API",
            log_type="ERROR",
            module="UPDATE-PROFILE",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Unexpected error",
            description=error_message
        )
        await sendLog(log)
        return 'error: ' + error_message, 400

async def DeleteProfile_handler(email):
    try:

        if not isValidToken(request, email):
            log = Log(
                app_name="PROFILE-API",
                log_type="ERROR",
                module="DELETE-PROFILE",
                log_date_time=datetime.datetime.now().isoformat(),
                summary="Failed to delete profile",
                description="Invalid token provided")
            await sendLog(log)
            return 'Error: Invalid token provided', 404

        profile = database.query(Profile).filter_by(email=email).first()

        if not profile:
            return 'Error: Profile not found', 404
        
        database.delete(profile)
        database.commit()

        log = Log(
            app_name="PROFILE-API",
            log_type="INFO",
            module="DELETE-PROFILE",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Profile deleted successfully",
            description="A profile has been deleted successfully"
        )
        await sendLog(log)
        return 'message: Profile deleted successfully', 200

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        log = Log(
            app_name="PROFILE-API",
            log_type="ERROR",
            module="DELETE-PROFILE",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Unexpected error",
            description=error_message
        )
        await sendLog(log)
        return 'error: ' + error_message, 400
    
async def GetProfile_handler(email):
    try:
        if not isValidToken(request, email):
            log = Log(
                app_name="PROFILE-API",
                log_type="ERROR",
                module="GET-PROFILE",
                log_date_time=datetime.datetime.now().isoformat(),
                summary="Failed to get profile",
                description="Invalid token provided")
            await sendLog(log)
            return {'error': 'Invalid token provided'}, 404

        profile = database.query(Profile).filter_by(email=email).first()

        if not profile:
            return {'error': 'Profile not found'}, 404

        profile_data = {
            'name': profile.name,
            'url': profile.url,
            'nickname': profile.nickname,
            'public_info': profile.public_info,
            'messaging': profile.messaging,
            'biography': profile.biography,
            'organization': profile.organization,
            'country': profile.country,
            'social_media': profile.social_media,
            'email': profile.email
        }

        log = Log(
            app_name="PROFILE-API",
            log_type="INFO",
            module="GET-PROFILE",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Profile retrieved successfully",
            description="A profile has been retrieved successfully"
        )
        await sendLog(log)
        return profile_data, 200

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        log = Log(
            app_name="PROFILE-API",
            log_type="ERROR",
            module="GET-PROFILE",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Unexpected error",
            description=error_message
        )
        await sendLog(log)
        return {'error': error_message}, 400


async def GetAllProfiles_handler():
    try:

        page = request.args.get('page', default=1, type=int)
        pagesize = request.args.get('pagesize', default=10, type=int)
        
        start_index = (page - 1) * pagesize
        end_index = start_index + pagesize

        profiles = database.query(Profile).slice(start_index, end_index).all()

        if not profiles:
            return 'No profiles found for the specified page', 404

        allProfiles = []
        for profile in profiles:
            serialized_profile = {
                'name': profile.name,
                'url': profile.url,
                'nickname': profile.nickname,
                'public_info': profile.public_info,
                'messaging': profile.messaging,
                'biography': profile.biography,
                'organization': profile.organization,
                'country': profile.country,
                'social_media': profile.social_media,
                'email': profile.email
            }
            allProfiles.append(serialized_profile)

        return allProfiles, 200

    except Exception as e:
        error_message = f'Unexpected error: {str(e)}'
        log = Log(
            app_name="PROFILE-API",
            log_type="ERROR",
            module="LIST-PROFILES",
            log_date_time=datetime.datetime.now().isoformat(),
            summary="Unexpected error",
            description=error_message
        )
        await sendLog(log)
        return 'error: ' + error_message, 400
