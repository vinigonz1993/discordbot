import React, { useState } from 'react';
import { Col, Form, InputGroup, Row } from 'react-bootstrap';
import styled from 'styled-components';
import { BtnPrimary } from '../common/Button';
import Request, { ParamsOCT } from '../requests';
import { COLORS } from '../common/Colors';

interface TripProps {
    time: string,
}

const Trip = styled.div<TripProps>`
    width: 100% !important;
    padding: 0.5em;
    font-size: 0.75em;
    ${(props) => {
        if (Number(props.time) < 10) {
            return `
                color: ${COLORS.dark};
                background: #cccf46;
            `;
        }
        return '';
    }}
`;

const OCT = () => {
    const [routes, setRoutes] = useState<[]>([]);
    const [trips, setTrips] = useState<[]>([]);
    const [stop, setStop] = useState<string>('1222');

    const getRoutes = () => {
        const params: ParamsOCT = {
            stopNo: stop,
        };

        Request.oct.get(params).then(
            (response) => setRoutes(response.data['GetRouteSummaryForStopResult']['Routes']['Route']),
        );
    }

    const handleClick = () => {
        getRoutes();
    };

    return (
        <>
            <Row>
                <Col>
                    <input
                        type="text"
                        onChange={(e) => setStop(e.target.value)}
                    />
                </Col>
                <Col>
                    <BtnPrimary
                        onClick={() => handleClick()}
                    >
                        Search Stop
                    </BtnPrimary>
                </Col>
            </Row>
            <hr />
            <Row>
                <Col xl={6} lg={6} md={6} sm={6} xs={6}>
                    {routes.map((route) => (
                        <BtnPrimary
                            key={`${route['RouteNo']} - ${route['RouteHeading']}`}
                            onClick={() => setTrips(route['Trips'])}
                        >
                            {route['RouteNo']} - {route['RouteHeading']}
                        </BtnPrimary>
                    ))}
                </Col>
                <Col xl={6} lg={6} md={6} sm={6} xs={6}>
                    {trips.length > 0 &&
                        trips.map((trip) => (
                            <Trip
                                time={trip['AdjustedScheduleTime']}
                            >
                                {trip['AdjustedScheduleTime']}min
                            </Trip>
                        ))
                    }
                </Col>
            </Row>
        </>
    );
};

export default OCT;
